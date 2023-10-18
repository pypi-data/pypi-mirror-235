"""Contains the `RichHandler` class.
"""

from __future__ import annotations
import re
from typing import IO, ClassVar, Literal, Mapping, Optional, Union
import logging
import sys

from rich.table import Table
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.traceback import Traceback
from rich.style import Style

from splatlog.lib import fmt
from splatlog.lib.rich import (
    Rich,
    is_rich,
    ntv_table,
    THEME,
    enrich,
    RichFormatter,
)
from splatlog.lib.typeguard import satisfies
from splatlog.splat_handler import SplatHandler
from splatlog.typings import (
    Level,
    RichThemeCastable,
    VerbosityLevelsCastable,
    StdioName,
    RichConsoleCastable,
)


class RichHandler(SplatHandler):
    """A `logging.Handler` extension that uses [rich][] to print pretty nice log
    entries to the console.

    Output is meant for specifically humans.
    """

    DEFAULT_THEME: ClassVar[Theme] = THEME

    @classmethod
    def cast_theme(cls, theme: object) -> Theme:
        if theme is None:
            # If no theme was provided create an instance-owned copy of the
            # default theme (so that any modifications don't spread to any other
            # instances... which usually doesn't matter, since there is
            # typically only one instance, but it's good practice I guess).
            return Theme(cls.DEFAULT_THEME.styles)

        if isinstance(theme, Theme):
            # Given a `rich.theme.Theme`, which can be used directly
            return theme

        if satisfies(theme, IO[str]):
            # Given an open file to read the theme from
            return Theme.from_file(theme)

        raise TypeError(
            "Expected `theme` to be {}, given {}: {}".format(
                fmt(Union[None, Theme, IO[str]]), fmt(type(theme)), fmt(theme)
            )
        )

    @classmethod
    def cast_console(
        cls, console: RichConsoleCastable, theme: Theme
    ) -> Console:
        if console is None:
            return Console(file=sys.stderr, theme=theme)

        if isinstance(console, Console):
            return console

        if satisfies(console, StdioName):
            return Console(
                file=(sys.stderr if console == "stderr" else sys.stdout),
                theme=theme,
            )

        if satisfies(console, IO[str]):
            return Console(file=console, theme=theme)

        raise TypeError(
            "expected `console` to be {}, given {}: {}".format(
                fmt(Union[Console, StdioName, IO[str]]),
                fmt(type(console)),
                fmt(console),
            )
        )

    console: Console
    formatter: RichFormatter

    def __init__(
        self,
        level: Level = logging.NOTSET,
        *,
        console: RichConsoleCastable = None,
        theme: RichThemeCastable = None,
        verbosity_levels: Optional[VerbosityLevelsCastable] = None,
        formatter: None | RichFormatter = None,
    ):
        super().__init__(level=level, verbosity_levels=verbosity_levels)

        self.theme = self.cast_theme(theme)
        self.console = self.cast_console(console, self.theme)

        if formatter is None:
            self.formatter = RichFormatter()
        else:
            self.formatter = formatter

    def emit(self, record):
        # pylint: disable=broad-except
        try:
            self._emit_table(record)
        except (RecursionError, KeyboardInterrupt, SystemExit):
            # RecursionError from cPython, they cite issue 36272; the other ones
            # we want to bubble up in interactive shells
            raise
        except Exception:
            # Just use the damn built-in one, it shouldn't happen much really
            #
            # NOTE  I _used_ to have this, and I replaced it with a
            #       `Console.print_exception()` call... probably because it
            #       sucked... but after looking at `logging.Handler.handleError`
            #       I realize it's more complicated to do correctly. Maybe it
            #       will end up being worth the effort and I'll come back to it.
            #
            self.handleError(record)

    def _get_rich_msg(self, record: logging.LogRecord) -> Rich:
        # If the record didn't come from a `splatlog.SplatLogger` (which adds
        # this special "extra" attribute) then defer to the standard message
        # formatting provided by `logging.LogRecord.getMessage`
        # (percent/printf-style interpolation), since that's what every other
        # logger will expect be using.
        #
        if not hasattr(record, "_splatlog_"):
            return Text(record.getMessage())

        # Get a "rich" version of `record.msg` to render
        #
        # NOTE  `str` instances can be rendered by Rich, but they do no count as
        #       "rich" -- i.e. `is_rich(str) -> False`.
        if is_rich(record.msg):
            # A rich message was provided, just use that.
            #
            # NOTE  In this case, any interpolation `args` assigned to the
            #       `record` are silently ignored because I'm not sure what we
            #       would do with them.
            return record.msg

        # `record.msg` is _not_ a Rich renderable; it is treated like a
        # string (like logging normally work).
        #
        # Make sure we actually have a string:
        msg = record.msg if isinstance(record.msg, str) else str(record.msg)

        # See if there are `record.args` to interpolate.
        if args := record.args:
            if isinstance(args, tuple):
                return self.formatter.vformat(msg, args, {})

            return self.formatter.vformat(msg, (), args)

        # Results are wrapped in a `rich.text.Text` for render, which is
        # assigned the `log.message` style (though that style is empty by
        # default).
        return Text.from_markup(msg, style="log.message")

    def _get_name_cell(self, record):
        text = Text()

        text.append(record.name, style="log.name")

        if class_name := getattr(record, "class_name", None):
            text.append(".", style="log.name")
            text.append(class_name, style="log.class")

        if (func_name := record.funcName) and func_name != "<module>":
            text.append(".", style="log.name")
            text.append(func_name, style="log.funcName")

        # Linking, only works on local vscode instance
        #
        # text.append(" ")
        # text.append(
        #     "📂",
        #     style=Style(
        #         link=f"vscode://file/{record.pathname}:{record.lineno}"
        #     ),
        # )

        return text

    def _emit_table(self, record):
        # SEE   https://github.com/willmcgugan/rich/blob/25a1bf06b4854bd8d9239f8ba05678d2c60a62ad/rich/_log_render.py#L26

        output = Table.grid(padding=(0, 1))
        output.expand = True

        # Left column -- log level, time
        output.add_column(width=8)

        # Main column -- log name, message, args
        output.add_column(ratio=1, overflow="fold")

        output.add_row(
            Text(
                record.levelname,
                style=f"logging.level.{record.levelname.lower()}",
            ),
            self._get_name_cell(record),
        )

        # output.add_row(
        #     Text("loc", style="log.label"), f"{record.pathname}:{record.lineno}"
        # )

        if src := getattr(record, "self", None):
            output.add_row(
                Text("self", style="log.label"),
                ntv_table(src) if isinstance(src, Mapping) else enrich(src),
            )

        output.add_row(
            Text("msg", style="log.label"), self._get_rich_msg(record)
        )

        if data := getattr(record, "data", None):
            output.add_row(Text("data", style="log.label"), ntv_table(data))

        if record.exc_info:
            output.add_row(
                Text("err", style="log.label"),
                Traceback.from_exception(*record.exc_info),
            )

        self.console.print(output)
