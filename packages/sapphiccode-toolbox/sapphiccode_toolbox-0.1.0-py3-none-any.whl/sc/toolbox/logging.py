import io
import logging
import sys
import typing

import click
import rich
import structlog
from rich.traceback import Traceback
from structlog.typing import EventDict, Processor, WrappedLogger

__all__ = [
    "logging_add_trace",
    "_configure_logging",
    "validate_log_level",
    "format_event_f_string",
    "ConsoleRenderer",
]


TRACE = logging.DEBUG - 1


def logging_add_trace():
    """
    Adds the TRACE level to `logging`.
    Does nothing if already present.
    """

    if isinstance(logging.getLevelName("TRACE"), str):
        logging.addLevelName(TRACE, "TRACE")


def format_event_f_string(
    logger: WrappedLogger, name: str, event_dict: EventDict
) -> EventDict:
    """
    Formats `event` with the event dictionary, using Python format string logic.
    """

    event_dict["event_unformatted"] = event_dict["event"]
    event_dict["event"] = event_dict["event"].format(**event_dict)
    return event_dict


class ConsoleRenderer:
    """
    A prettier `structlog.dev.ConsoleRenderer`. [citation needed]
    """

    def __init__(
        self,
        *,
        priority_fields: typing.List[str] = ["timestamp", "level", "logger", "event"],
        omit_fields: typing.List[str] = [],
        field_separator="  ",
        event_padding: int = 32,
    ):
        self.priority_fields = priority_fields
        self.omit_fields = omit_fields

        self.field_separator = field_separator
        self.event_padding = event_padding

        self.console = rich.console.Console(force_terminal=True)

    def _render_field(self, field: str, event_dict: EventDict) -> str:
        data = event_dict.get(field)
        if not data:
            return ""

        if field == "timestamp":
            return f"[grey11]{data}[/grey11]{self.field_separator}"
        if field == "level":
            level_colors = {
                "critical": "bright_red",
                "error": "bright_red",
                "warning": "orange_red1",
            }
            color = level_colors.get(data, "bright_blue")
            return (
                f"[bold {color}]{data.upper(): <8}[/bold {color}]{self.field_separator}"
            )
        if field == "logger":
            return f"[orange1]{data}[/orange1]{self.field_separator}"
        if field == "event":
            return (
                f"[bold bright_cyan]{data: <{self.event_padding}}[/bold bright_cyan]"
                + self.field_separator
            )

        return f"[green]{field}[/green]=[sea_green3]{data}[/sea_green3] "

    def __call__(self, logger: WrappedLogger, name: str, event_dict: EventDict) -> str:
        fields_already_rendered: typing.Set[str] = set()

        exc_info = event_dict.pop("exc_info", None)
        out = ""

        # render prioritized fields
        for field in self.priority_fields:
            out += self._render_field(field, event_dict)
            fields_already_rendered.add(field)

        # render remaining fields
        for field in event_dict:
            if field in fields_already_rendered or field in self.omit_fields:
                continue

            out += self._render_field(field, event_dict)

        # set up output
        sio = io.StringIO()
        self.console.file = sio
        self.console.print(out.rstrip(), highlight=False)
        if exc_info:
            if isinstance(exc_info, Exception):
                exc_info = exc_info.__class__, exc_info, exc_info.__traceback__
            assert isinstance(exc_info, tuple)
            self.console.print(Traceback.from_exception(*exc_info))

        return sio.getvalue().rstrip()


def _configure_logging(
    level: int = logging.INFO, root_level: int = logging.INFO
) -> None:
    """
    Configures the logging system for toolbox.
    """

    shared_processors: typing.List[Processor] = [
        structlog.processors.TimeStamper("iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_log_level_number,
    ]

    if not logging.root.handlers:
        handler = logging.StreamHandler()

        # determine output renderer
        renderer: typing.List[Processor] = [
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ]
        if sys.stderr.isatty():
            renderer = [
                ConsoleRenderer(
                    omit_fields=[
                        "event_unformatted",
                        "level_number",
                    ]
                )
            ]

        handler.setFormatter(
            structlog.stdlib.ProcessorFormatter(
                foreign_pre_chain=shared_processors,
                processors=[
                    structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                    *renderer,
                ],
            )
        )
        logging.root.addHandler(handler)

    logging.root.setLevel(root_level)
    logging.getLogger("sc.toolbox").setLevel(level)

    if not structlog.is_configured():
        structlog.configure(
            processors=shared_processors
            + [
                format_event_f_string,
                structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
        )

    logging.getLogger(__name__).debug("Hello from stdlib.")
    structlog.stdlib.get_logger().debug("Hello from structlog.")


def validate_log_level(ctx: click.Context, param: click.Parameter, value: str) -> int:
    """Validates and returns an integer log level for Click."""

    logging_add_trace()

    level = logging.getLevelName(value.upper())
    if not isinstance(level, int):
        raise TypeError("Invalid log level.")
    return level
