from __future__ import annotations

import argparse
import logging
import sys
import textwrap

from .cls import DownloadLatest, DownloadLatestException
from .fetch import DEFAULT_FETCH_BACKEND, FETCH_BACKENDS
from .meta import __program__, __version__
from .util import COLORS


__all__ = ["Console", "ConsoleFormatter", "main"]


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
        color = parser.add_mutually_exclusive_group()
        color.add_argument(
            "-c",
            "--color",
            action="store_true",
            default=None,
            help="enable colorized output",
        )
        color.add_argument(
            "-C",
            "--no-color",
            action="store_false",
            help="disable colorized output",
            dest="color",
        )
        progress = parser.add_mutually_exclusive_group()
        progress.add_argument(
            "-p",
            "--progress",
            action="store_true",
            default=None,
            help="enable the progress meter",
        )
        progress.add_argument(
            "-P",
            "--no-progress",
            action="store_false",
            help="disable the progress meter",
            dest="progress",
        )
        parser.add_argument(
            "--backend",
            choices=FETCH_BACKENDS,
            default=DEFAULT_FETCH_BACKEND,
            help=f"how to download (default: {DEFAULT_FETCH_BACKEND})",
            metavar="BACKEND",
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

    @classmethod
    def main(cls) -> None:
        """The main function called from the CLI."""
        a = cls.get_args(args=None, isatty=sys.stdin.isatty())
        logger = cls.get_logger(quiet=a.quiet, verbose=a.verbose, color=a.color)
        try:
            DownloadLatest(
                url=a.url,
                backend=a.backend,
                file=a.file,
                dry_run=a.dry_run,
                force=a.force,
                logger=logger,
                meter=a.progress,
            ).run()
        except (DownloadLatestException, OSError) as e:
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


def main() -> None:  # pragma: no cover
    Console.main()
