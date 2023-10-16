from __future__ import annotations

import os
from pathlib import Path
import shutil
import sys
from typing import ClassVar, TextIO

from .spinner import Spinner
from .util import COLORS, HumanNumberFormatter, get_file_size


__all__ = [
    "DownloadMeter",
    "DownloadWithRemoteMeter",
    "DownloadWithoutRemoteMeter",
    "HeadMeter",
    "Meter",
]


class Meter:
    """A progress meter."""

    PERIOD: ClassVar[float] = 1 / 15

    output: TextIO

    def __init__(self, output: TextIO | None = None) -> None:
        """Create the meter."""
        self.output = sys.stdout if output is None else output

    def begin(self) -> None:
        """Run at the beginning."""
        raise NotImplementedError()

    def end(self) -> None:
        """Run at the end."""
        raise NotImplementedError()

    def period(self) -> float:
        """Return the period time in seconds."""
        return self.PERIOD

    def step(self) -> None:
        """Run at each interval."""
        raise NotImplementedError()

    def write(self, text: str) -> None:
        """Write output, usually to stdout."""
        print(text, end="", file=self.output, flush=True)

    @classmethod
    def get(
        cls,
        output: TextIO | None = None,
        path: os.PathLike | str | None = None,
        remote_size: int | None = None,
    ):
        """Return the appropriate meter."""
        if path is None:
            return HeadMeter(output=output)
        elif remote_size is None:
            return DownloadWithoutRemoteMeter(
                output=output,
                path=path,
            )
        else:
            return DownloadWithRemoteMeter(
                output=output,
                path=path,
                remote_size=remote_size,
            )


class DownloadMeter(Meter):
    """Base class for both DownloadMeters."""

    DEFAULT_SCREEN_WIDTH: ClassVar[int] = 80
    SPINNER_CHARS: ClassVar[str] = "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁"

    path: Path
    spinner: Spinner

    def __init__(self, *args, path: os.PathLike | str, **kwargs) -> None:
        """Create the meter."""
        super().__init__(*args, **kwargs)
        self.path = Path(path)
        self.spinner = Spinner(
            chars=self.SPINNER_CHARS,
            width=self.DEFAULT_SCREEN_WIDTH,
            step=1,
        )

    def begin(self) -> None:
        """Run at the beginning."""
        self.write("\r\x1b[2K")
        self.step()

    def end(self) -> None:
        """Run at the end."""
        self.step()
        self.write("\n")

    def get_current_size(self):
        """Return the current size of path."""
        return get_file_size(self.path) or 0

    def get_screen_width(self) -> int:
        """Return the current screen width."""
        screen_width, _ = shutil.get_terminal_size((self.DEFAULT_SCREEN_WIDTH, 1))
        return screen_width

    def get_progress(self, progress: float, offset: int) -> str:
        """Return the progress bar."""
        available_width = self.get_screen_width() - (offset + 3)
        self.spinner.width = round(progress * available_width)
        # TODO: this should only output color if --color is specified
        return (
            "["
            + COLORS.BLUE24
            + f"{next(self.spinner):<{available_width}}"
            + COLORS.RESET
            + "]"
        )


class DownloadWithRemoteMeter(DownloadMeter):
    """A download meter when we know the remote size."""

    formatter: HumanNumberFormatter
    remote_size: int

    def __init__(self, *args, remote_size: int, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.remote_size = remote_size if remote_size > 0 else 1
        self.formatter = HumanNumberFormatter.suggest(remote_size, width=4)

    def step(self) -> None:
        current_size = self.get_current_size()
        progress = min(1.0, current_size / self.remote_size)
        status = self.formatter.format_with_total(current_size, self.remote_size)
        status_width = max(11, len(status))
        status = f"{status:>{status_width}} {(100*progress):>3.0f}%"
        self.write(f"\r{self.get_progress(progress, len(status))}{status}")


class DownloadWithoutRemoteMeter(DownloadMeter):
    """The meter for download requests when we don't know the remote size."""

    def step(self) -> None:
        current_size = self.get_current_size()
        status = HumanNumberFormatter.format_number(current_size, width=6)
        status = f"{status:>8}"
        self.write(f"\r{self.get_progress(1.0, len(status))}{status}")


class HeadMeter(Meter):
    """The meter for head requests."""

    SPINNER_CHARS: ClassVar[str] = "/-\\|"

    spinner: Spinner

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.spinner = Spinner(chars=self.SPINNER_CHARS, width=1, step=1)

    def begin(self) -> None:
        self.write("\r\x1b[2K")
        self.step()

    def end(self) -> None:
        self.write("\r\x1b[2K")

    def step(self) -> None:
        self.write(f"\r request: {next(self.spinner)} \x1b[0K")
