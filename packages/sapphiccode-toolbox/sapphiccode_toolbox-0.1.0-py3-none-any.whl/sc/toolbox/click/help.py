"""
Adjusted command help generators for [click](https://click.palletsprojects.com/en/).
"""


import typing as t

import click
from click.core import Context
from click.formatting import HelpFormatter


def _all_command_contexts(
    root: click.Group,
    ctx: click.Context,
) -> t.Generator[click.Context, None, None]:
    """
    Recursively iterates over a command group, yielding contexts for every command.
    """

    for command_name in root.list_commands(ctx):
        command = root.get_command(ctx, command_name)
        if command is None:
            continue
        if command.hidden:
            continue

        yield Context(command, ctx)

        if isinstance(command, click.Group):
            yield from _all_command_contexts(
                command,
                Context(command, ctx),
            )


def _canonical_command_name(ctx: Context) -> str:
    """
    Attempts to create a full command name path by following contexts.
    """

    if ctx.command.name is None:
        return ""

    parents = [ctx.command.name]

    parent = ctx.parent
    while parent is not None and parent is not parent.find_root():
        if parent.command.name is not None:
            parents.append(parent.command.name)
        parent = parent.parent

    return " ".join(parents[::-1])


class RecursivelyRenderSubcommandsGroup(click.Group):
    """
    A click Group-compatible class that changes the help renderer to recursively
    list commands.
    """

    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None:
        contexts = _all_command_contexts(self, ctx)
        with formatter.section("Commands"):
            formatter.write_dl(
                [
                    (_canonical_command_name(x), x.command.get_short_help_str())
                    for x in contexts
                    if not isinstance(x.command, click.Group)
                ]
            )

        # TODO: render groups if len(subcommands) > 1, else recursive render
        # TODO: render groups if there are required options on a group?
