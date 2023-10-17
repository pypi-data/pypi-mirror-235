import os
import shutil
import subprocess
import tempfile
import textwrap
import typing

import click
import rich
import structlog
import yaml

from ...config.base import ToolboxConfigSpec
from ...config.image_border import ANCHORS, EDGES, ImageBorderConfig
from ...exiftool import exiftool, exiftool_json, supplement_tags

LOG = structlog.stdlib.get_logger()


@click.command(
    short_help="Adds a border to an image with arbitrary text",
    help="""
    Adds an informational border to an input image based on EXIF metadata.

    Outputs the path of the new image.

    \b
    Soft dependencies:
    - ExifTool:       image border templating, preservation of EXIF data to output
    - ImageMagick:    higher quality output options
    - GraphicsMagick: alternative support for ImageMagick

    \b
    Configuration options with their defaults (represented here in YAML):
    """.rstrip()
    + "\n"
    + textwrap.indent(
        yaml.safe_dump(
            ImageBorderConfig().model_dump(mode="json"),
            sort_keys=False,
        ),
        " " * 6,
    ),
)
@click.pass_context
@click.argument(
    "path",
    type=click.Path(exists=True, dir_okay=False),
)
@click.option(
    "-o",
    "--output",
    type=click.Path(writable=True),
    default=None,
    help="Write to the specified file.",
)
def border(
    ctx: click.Context,
    path: str,
    output: typing.Optional[str],
):
    # verify dependencies
    try:
        from PIL import Image, ImageColor, ImageDraw, ImageFont
    except ImportError as e:
        e.add_note("You might need to reinstall toolbox with `sc-toolbox[image]`.")
        raise

    console = rich.console.Console(stderr=True)

    exif_enable = bool(shutil.which("exiftool"))
    magick = shutil.which("gm") or shutil.which("magick")

    # load config
    root_config = ctx.find_object(ToolboxConfigSpec)
    assert root_config is not None
    config = root_config.image.border

    status = console.status("Loading file...")
    status.start()
    # copy input
    tmp_in = tempfile.NamedTemporaryFile(suffix=os.path.basename(path))
    shutil.copyfile(path, tmp_in.name)

    # set output extension correctly
    ext_out = ""
    ext_in = tmp_in.name.split(".")[-1].upper()
    if ext_in != config.output_format and {ext_in, config.output_format} != {
        "JPG",
        "JPEG",
    }:
        ext_out = f".{config.output_format}"

    tmp_out = tempfile.NamedTemporaryFile(
        suffix=os.path.basename(path) + ext_out, delete=bool(output)
    )

    # read EXIF metadata
    if exif_enable:
        exif = supplement_tags(exiftool_json(tmp_in.name))
    else:
        exif = {}
        LOG.warning("ExifTool not found. No tags available for templating.")

    # auto-rotate input image if magick is available
    if magick:
        subprocess.check_call((magick, "mogrify", "-auto-orient", tmp_in.name))

    # manipulate image
    status.update("Manipulating image...")
    with Image.open(tmp_in.name) as picture:
        border = max(
            int(max(picture.size) * config.border_percent * 0.01),
            config.border_minimum_px,
        )
        img = Image.new(
            picture.mode,
            (picture.size[0] + border * 2, picture.size[1] + border * 2),
            color=ImageColor.getrgb(config.border_color),
        )

        img.paste(picture, box=(border, border))

        # draw text
        im_text = Image.new(
            "RGB",
            size=(picture.size[EDGES[config.text_edge][1]], border),
            color=config.border_color,
        )
        d = ImageDraw.Draw(im_text)
        font = ImageFont.truetype(
            config.text_font, int(border * config.text_height_percent * 0.01)
        )
        text_color = ImageColor.getrgb(config.text_color)
        text_y = int(border * ANCHORS[config.text_vertical_anchor][1])

        try:
            for pos, element in config.elements_l.items():
                d.text(
                    xy=(
                        pos * border,  # border + shift
                        text_y,
                    ),
                    anchor="l" + ANCHORS[config.text_vertical_anchor][0],
                    text=element.format(**exif),
                    font=font,
                    fill=text_color,
                )

            for pos, element in config.elements_r.items():
                d.text(
                    xy=(
                        im_text.size[0] - (pos * border),
                        text_y,
                    ),
                    anchor="r" + ANCHORS[config.text_vertical_anchor][0],
                    text=element.format(**exif),
                    font=font,
                    fill=text_color,
                )
        except KeyError as e:
            LOG.error(
                "Could not template a text field.",
                available_tags=list(exif),
                exc_info=e,
            )
            raise click.Abort()

        im_text = im_text.rotate(EDGES[config.text_edge][0], expand=True)
        img.paste(im_text, EDGES[config.text_edge][2](border, picture.size))

    status.update("Writing output...")
    # save
    if magick and config.output_format in {"JPEG"}:
        # use ImageMagick to save if possible, uses libjpeg for better quality
        with tempfile.NamedTemporaryFile(suffix=".bmp") as tmp_magick:
            img.save(tmp_magick.name, format="BMP")
            subprocess.check_call(
                (
                    magick,
                    "convert",
                    tmp_magick.name,
                    "-quality",
                    str(config.output_quality),
                    tmp_out.name,
                )
            )
    else:
        LOG.warning(
            "ImageMagick not found. "
            "Using Pillow's native encoder instead, "
            "this might have quality implications."
        )
        img.save(
            tmp_out.name,
            format=config.output_format,
            quality=config.output_quality,
        )

    # re-attach exif metadata
    if exif_enable and config.output_format not in {"BMP"}:
        exiftool(
            "-tagsfromfile",
            tmp_in.name,
            "-all:all",
            "-Software<$Software, sapphiccode-toolbox",
            tmp_out.name,
            stdout=subprocess.DEVNULL,
        )
        os.remove(tmp_out.name + "_original")  # clean up exiftool backup file

    if not output:
        print(tmp_out.name)
    else:
        shutil.copyfile(
            tmp_out.name,
            output,
        )
        print(output)

    status.update("Cleaning up...")

    tmp_in.close()
    tmp_out.close()
    status.stop()
