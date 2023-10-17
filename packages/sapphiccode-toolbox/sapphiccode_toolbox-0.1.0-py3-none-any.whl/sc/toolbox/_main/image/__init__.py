import click

from .border import border


@click.group
def image():
    """Image manipulation commands"""
    pass


image.add_command(border)
