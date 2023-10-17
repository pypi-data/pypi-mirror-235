import hashlib
import os
import shutil
import typing

import click
import rich
import structlog
import tqdm
from rich.prompt import Confirm

LOG = structlog.stdlib.get_logger()


@click.command
@click.option(
    "-b",
    "--blob-store",
    default=None,
    show_default=".blobs",
    type=click.Path(writable=True),
    help="Where to move the real file contents to.",
)
@click.option(
    "--hash",
    "htype",
    default="sha256",
    show_default=True,
    type=click.Choice(sorted(hashlib.algorithms_available)),
    help="The hash to be used.",
)
@click.option(
    "--relative/--absolute",
    default=True,
    show_default=True,
    help="The type of symlinks to emit.",
)
@click.argument("paths", type=click.Path(exists=True), nargs=-1, required=True)
def hashlink(
    relative: bool,
    htype: str,
    blob_store: typing.Optional[str],
    paths: typing.List[str],
):
    """
    Hashes files and replaces them with symlinks.

    Converts input PATHS containing files to a path containing only symbolic links
    to files with hashes for names.

    Caution: blob store will be created in current directory unless -b is specified.
    """

    console = rich.console.Console(stderr=True)

    with console.status("Indexing...") as status:
        files: typing.List[str] = []
        for path in paths:
            for dirpath, dirnames, filenames in os.walk(path):
                for fname in filenames:
                    fpath = os.path.join(dirpath, fname)
                    if os.path.isfile(fpath) and not os.path.islink(fpath):
                        files.append(fpath)
                status.update(f"Indexing... [{len(files)}]")

    LOG.info("Discovered {n} files.", n=len(files))

    if blob_store is None:
        if not os.path.exists(".blobs"):
            if not Confirm.ask("Create new blob store?"):
                raise click.Abort()

        blob_store = ".blobs"
        os.makedirs(blob_store, exist_ok=True)

    for file in tqdm.tqdm(files):
        hasher = hashlib.new(htype)

        # hash file
        with open(file, "rb") as f:
            while data := f.read(1024 * 1024):
                hasher.update(data)

        # move to .blobs/<hexdigest>
        hexdigest = hasher.hexdigest()
        blob_file = os.path.join(blob_store, hexdigest)
        if not os.path.isfile(blob_file):
            shutil.move(file, blob_file)
        else:
            os.remove(file)

        # create symlink
        if relative:
            target = os.path.relpath(blob_file, os.path.dirname(file))
        else:
            target = os.path.abspath(blob_file)
        os.symlink(target, file)
