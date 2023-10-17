import click

from .hashlink import hashlink


@click.group
def archive():
    """File archival utilities"""


archive.add_command(hashlink)
