import typing

import click

from ..config import _get_config
from ..logging import _configure_logging, validate_log_level
from .archive import archive
from .image import image


@click.group
@click.pass_context
@click.option(
    "--log-level",
    help="Sets the log level for toolbox.",
    type=str,
    default="INFO",
    show_default=True,
    callback=validate_log_level,
)
@click.option(
    "--log-level-tp",
    help="Sets the log level for third-party loggers.",
    type=str,
    default="INFO",
    show_default=True,
    callback=validate_log_level,
)
@click.option(
    "-c",
    "--config",
    type=click.Path(),
    multiple=True,
    help="Prioritized configuration search paths.",
)
def main(
    ctx: click.Context,
    log_level: int,
    log_level_tp: int,
    config: typing.List[str],
):
    """
    Cassandra's toolbox

    A bunch of utilities that probably don't mean anything to anyone else.
    """

    _configure_logging(log_level, log_level_tp)
    ctx.obj = _get_config(config)


for command in {
    image,
    archive,
}:
    main.add_command(command)
