from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path
import shutil
import sys
import textwrap
from typing import ClassVar, TextIO

from .cls import DownloadLatest, DownloadLatestException
from .fetch import DEFAULT_FETCH_BACKEND, FETCH_BACKENDS, FetchMeter
from .meta import __program__, __version__
from .spinner import Spinner
from .util import COLORS, HumanNumberFormatter, get_file_size


__all__ = [
    "Console",
    "ConsoleFormatter",
    "ProgressMeter",
    "main",
]


class Console:
    """Console method wrapper."""

    @staticmethod
    def get_args(
        args: list | None = None,
        isatty: bool = False,
    ) -> argparse.Namespace:
        """Return the parsed arguments for the CLI."""

        USAGE = "%(prog)s [ -h | --help ] [OPTIONS] URL [FILE]"
        DESCRIPTION = "Download URL to FILE only if remote file has changed."
        HUMAN_FETCH_BACKENDS = repr(FETCH_BACKENDS)[1:-1].replace("'p", "or 'p")
        EPILOG = textwrap.dedent(
            f"""\
            BACKEND can be one of {HUMAN_FETCH_BACKENDS}. If 'auto', then 'curl'
            will be chosen if available, otherwise fallback to 'python'.

            If the color or progress options are not specified, they are determined
            from the TTY.

            If FILE is not specified, it will be deduced by the filename part of the
            URL. If no filename can be deduce, e.g., https://example.com/, then the
            program will exit with an error.

            Additional files may be generated:

            FILE.new       present when download occured, otherwise absent
            FILE.download  in-progress download
            """
        )

        parser = argparse.ArgumentParser(
            prog=__program__,
            usage=USAGE,
            description=DESCRIPTION,
            epilog=EPILOG,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        parser.add_argument(
            "url",
            help="url to download",
            metavar="URL",
        )
        parser.add_argument(
            "file",
            nargs="?",
            help="path to output (deduced if not specified, see below)",
            metavar="FILE",
        )
        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version=f"{__program__} {__version__}",
        )
        parser.add_argument(
            "-n",
            "--dry-run",
            action="store_true",
            help="do not download (default: false)",
        )
        parser.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="do not check for changes (default: false)",
        )
        verbosity = parser.add_mutually_exclusive_group()
        verbosity.add_argument(
            "-q",
            "--quiet",
            action="store_true",
            help="suppress output (default: false)",
        )
        verbosity.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            help="increase output (default: false)",
        )
        parser.add_argument(
            "--backend",
            choices=FETCH_BACKENDS,
            default=DEFAULT_FETCH_BACKEND,
            help=f"how to download (default: {DEFAULT_FETCH_BACKEND})",
            metavar="BACKEND",
        )
        color = parser.add_mutually_exclusive_group()
        color.add_argument(
            "--color",
            action="store_true",
            default=None,
            help="enable colorized output",
        )
        color.add_argument(
            "--no-color",
            action="store_false",
            help="disable colorized output",
            dest="color",
        )
        progress = parser.add_mutually_exclusive_group()
        progress.add_argument(
            "--progress",
            action="store_true",
            default=None,
            help="enable the progress meter",
        )
        progress.add_argument(
            "--no-progress",
            action="store_false",
            help="disable the progress meter",
            dest="progress",
        )

        # https://docs.python.org/3/library/argparse.html#intermixed-parsing
        parsed_args = parser.parse_intermixed_args(args)

        if parsed_args.color is None:
            parsed_args.color = isatty
        if parsed_args.progress is None:
            parsed_args.progress = isatty

        return parsed_args

    @staticmethod
    def get_logger(
        quiet: bool = False,
        verbose: bool = False,
        color: bool = True,
        name: str = __name__,
    ) -> logging.Logger:
        """
        Return the logger for the CLI.

        If quiet is set, then logger is mute. Otherwise, two handlers are added
        such that:

        - Messages of WARNING, ERROR and CRITICAL levels are sent to stderr.
        - Messages of INFO (and DEBUG if verbose) levels are sent to stdout.
        """

        logger = logging.getLogger(name)

        if quiet:
            logger.setLevel(logging.CRITICAL + 1)
            logger.addHandler(logging.NullHandler())
            return logger

        if verbose:
            min_level = logging.DEBUG
        else:
            min_level = logging.INFO

        class StdOutFilter(logging.Filter):
            def filter(self, record):
                return min_level <= record.levelno and record.levelno < logging.WARNING

        formatter = ConsoleFormatter(color=color)
        stdout_handler = logging.StreamHandler(stream=sys.stdout)
        stderr_handler = logging.StreamHandler(stream=sys.stderr)
        stdout_handler.setFormatter(formatter)
        stderr_handler.setFormatter(formatter)
        stdout_handler.addFilter(StdOutFilter())
        stderr_handler.setLevel(logging.WARNING)
        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    @staticmethod
    def get_meter(quiet: bool = False, progress: bool = False) -> ProgressMeter | None:
        """Return a ProgresMeter under the right conditions."""
        if not quiet and progress:
            return ProgressMeter()
        else:
            return None

    @classmethod
    def main(cls) -> None:
        """The main function called from the CLI."""
        a = cls.get_args(args=None, isatty=sys.stdin.isatty())
        logger = cls.get_logger(quiet=a.quiet, verbose=a.verbose, color=a.color)
        meter = cls.get_meter(quiet=a.quiet, progress=a.progress)
        try:
            DownloadLatest(
                url=a.url,
                backend=a.backend,
                file=a.file,
                dry_run=a.dry_run,
                force=a.force,
                logger=logger,
                meter=meter,
            ).run()
        except DownloadLatestException as e:
            logger.error(f"   error: {e!s}")
            sys.exit(32)
        except OSError as e:
            logger.error(f"   error: {e!s}")
            sys.exit(1)
        except KeyboardInterrupt:
            logger.warning("keyboard interrupt")
            sys.exit(130)
        except Exception as e:
            logger.critical(f"   error: {e!r}")
            raise e


class ConsoleFormatter(logging.Formatter):
    """A simple logging formatter supporting colors."""

    def __init__(self, *args, color: bool = False, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.color = color

    def format(self, record: logging.LogRecord) -> str:
        """Format the record using colors if requested."""
        formatted = super().format(record)
        if self.color:
            if formatted.startswith(" success"):
                msg_color = COLORS.GREEN + COLORS.BOLD
            elif record.levelno <= logging.DEBUG:
                msg_color = ""
            elif record.levelno <= logging.INFO:
                msg_color = COLORS.BOLD
            elif record.levelno <= logging.WARNING:
                msg_color = COLORS.ORANGE214 + COLORS.BOLD
            else:
                msg_color = COLORS.RED160 + COLORS.BOLD
            reset = COLORS.RESET
        else:
            msg_color = reset = ""
        return f"{msg_color}{formatted}{reset}"


class ProgressMeter(FetchMeter):
    DEFAULT_SCREEN_WIDTH: ClassVar[int] = 80
    PERIOD: ClassVar[float] = 1 / 10
    PROBE_CHARS: ClassVar[str] = "/-\\|"
    WAVE_CHARS: ClassVar[str] = "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁"

    output: TextIO
    probe: Spinner
    wave: Spinner

    formatter: HumanNumberFormatter
    path: Path | None
    remote_size: int | None
    start_size: int | None

    def __init__(self, output: TextIO | None = None) -> None:
        self.output = sys.stdout if output is None else output
        screen_width = self.get_screen_width()
        self.probe = Spinner(chars=self.PROBE_CHARS, width=1, step=1)
        self.wave = Spinner(chars=self.WAVE_CHARS, width=screen_width, step=1)
        self.formatter = HumanNumberFormatter.suggest(100_000_000, width=6)
        self.path = None
        self.remote_size = None
        self.start_size = None

    def period(self) -> float:
        return self.PERIOD

    def begin(
        self,
        path: os.PathLike | str | None = None,
        remote_size: int | None = None,
    ) -> None:
        self.path = Path(path) if path else None
        self.remote_size = remote_size
        self.start_size = (get_file_size(self.path) or 0) if self.path else None
        if remote_size:
            self.formatter = HumanNumberFormatter.suggest(remote_size, width=4)

        self.write("\r\x1b[2K")
        self.progress()

    def step(self, index: int) -> None:
        self.progress()

    def end(self) -> None:
        self.progress()
        if self.path:
            self.write("\n")
        else:
            self.write("\r\x1b[2K")

    def progress(self) -> None:
        if self.path:
            if self.remote_size:
                self.progress_with_remote_size()
            else:
                self.progress_without_remote_size()
        else:
            self.progress_probe()

    def progress_probe(self) -> None:
        self.write(f"\r request: {next(self.probe)} \x1b[0K")

    def progress_with_remote_size(self) -> None:
        current_size = (get_file_size(self.path) or 0) if self.path else 0
        total_size = self.remote_size or 1
        complete = min(1.0, current_size / total_size)

        status = self.formatter.format_with_total(current_size, total_size)
        status_width = max(11, len(status))
        extra = f"{status:>{status_width}} {(100*complete):>3.0f}%"
        self.write(f"{self.get_wave(complete, len(extra))}{extra}")

    def progress_without_remote_size(self) -> None:
        current_size = (get_file_size(self.path) or 0) if self.path else 0
        status = HumanNumberFormatter.format_number(current_size, width=6)
        extra = f"{status:>8}"
        self.write(f"{self.get_wave(1.0, len(extra))}{extra}")

    def get_wave(self, complete: float, extra_width: int) -> str:
        available = self.get_screen_width() - (extra_width + 3)
        self.wave.width = round(complete * available)
        wave = next(self.wave)
        return f"\r[{COLORS.BLUE24}{wave:<{available}}{COLORS.RESET}]"

    def write(self, text: str):
        print(text, end="", file=self.output, flush=True)

    def get_screen_width(self) -> int:
        screen_width, _ = shutil.get_terminal_size((self.DEFAULT_SCREEN_WIDTH, 1))
        return screen_width


def main() -> None:  # pragma: no cover
    Console.main()
