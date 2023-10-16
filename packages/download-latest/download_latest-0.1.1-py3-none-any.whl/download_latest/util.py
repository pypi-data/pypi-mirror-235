"""
Standalone utility methods.
"""

from __future__ import annotations

import base64
import dataclasses
from datetime import datetime, timezone
import email.message
import hashlib
import locale
import os
from pathlib import Path
import re
import shlex
from typing import ClassVar, Sequence, TypeVar
import urllib.parse

from .meta import __program__


__all__ = [
    "COLORS",
    "HumanNumberFormatter",
    "deduce_filename_from_url",
    "get_file_md5",
    "get_file_modified",
    "get_file_size",
    "get_human_args",
    "get_human_file_size",
    "get_human_time",
    "get_user_cache_dir",
    "parse_header_accept_ranges",
    "parse_header_content_length",
    "parse_header_content_md5",
    "parse_header_etag",
    "parse_header_last_modified",
    "rm_f",
    "sanitize_filename",
    "truncate",
    "urllib_safe_url",
]


class COLORS:
    # https://stackoverflow.com/a/33206814
    GREY243 = "\x1b[38;5;243m"
    ORANGE214 = "\x1b[38;5;214m"
    RED160 = "\x1b[38;5;160m"
    GREEN = "\x1b[0;32m"
    BLUE24 = "\x1b[38;5;24m"
    BOLD = "\x1b[1m"
    RESET = "\x1b[0m"


@dataclasses.dataclass
class HumanNumberFormatter:
    """Convinience class for formatting numbers."""

    TABLE: ClassVar[str] = "BKMGTPEZY"

    base: int
    e: int
    precision: int
    unit: str
    width: int

    def format(self, n: int, with_unit: bool = True) -> str:
        """Return a formatted number."""
        unit = self.unit if with_unit else ""
        return f"{(n / self.base):.{self.precision}f}{unit}"

    def format_with_total(
        self,
        n: int,
        total: int,
        separator: str = "/",
        with_unit: bool = True,
    ) -> str:
        """
        Return a 'N/TOTAL' formatted pair of numbers.
        """
        return (
            self.format(n, with_unit=False)
            + separator
            + self.format(total, with_unit=with_unit)
        )

    @classmethod
    def suggest(cls, limit: int, width: int) -> HumanNumberFormatter:
        """
        Return a suggested HumanNumberFormat for a particular limit and width.
        Note, the resultant format width may be less than the requested width.
        """

        if limit < 0:
            raise ValueError("limit must be >= 0")
        if width < 3:
            raise ValueError("width must be >= 3")

        if limit < 1000 or (limit < 10000 and width >= 4):
            e = 0
            precision = 0
        else:
            if width == 3:
                p2_cmp = 0.0
                p1_cmp = 9.95
                p0_cmp = 999.5
            elif width == 4:
                p2_cmp = 0.0
                p1_cmp = 99.95
                p0_cmp = 9999.5
            elif width == 5:
                p2_cmp = 99.995
                p1_cmp = 999.95
                p0_cmp = 9999.5
            elif width == 6:
                p2_cmp = 999.995
                p1_cmp = 9999.95
                p0_cmp = 0.0
            else:  # width >= 7
                p2_cmp = 9999.995
                p1_cmp = 0.0
                p0_cmp = 0.0
            e = 1
            while True:
                d = limit / 1024**e
                if d < p2_cmp:
                    precision = 2
                    break
                elif d < p1_cmp:
                    precision = 1
                    break
                elif d < p0_cmp:
                    precision = 0
                    break
                e += 1

        return cls(
            base=1024**e,
            e=e,
            precision=precision,
            unit=cls.TABLE[e],
            width=len(f"{limit / 1024**e:.{precision}f}"),
        )

    @classmethod
    def format_number(cls, n: int, width: int = 5, with_unit: bool = True) -> str:
        formatter = cls.suggest(limit=n, width=width)
        return formatter.format(n, with_unit=with_unit)


def deduce_filename_from_url(url: str, os_name: str = "auto") -> str | None:
    """
    Deduce and return a filename from url. Return None if not possible.

    If os_name is 'auto', then use os.name.
    """
    purl = urllib.parse.urlparse(url)
    if not purl.scheme:
        purl = urllib.parse.urlparse(f"http://{url}")
    path = purl._replace(scheme="", netloc="").geturl()
    parts = path.split("/")
    while parts:
        if parts[-1] in ("", "."):
            parts.pop()
        elif parts[-1] == "..":
            parts.pop()
            if parts:
                parts.pop()
        else:
            break
    if parts:
        return sanitize_filename(parts[-1], os_name=os_name)
    else:
        return None


def get_file_md5(path: os.PathLike | str) -> str | None:
    """Return the MD5 hexdigest of path."""
    MD5_BUFFER_SIZE = 32768
    hash = hashlib.md5()
    try:
        with Path(path).open("rb") as f:
            while True:
                buffer = f.read(MD5_BUFFER_SIZE)
                if buffer:
                    hash.update(buffer)
                else:
                    break
            return hash.hexdigest()
    except FileNotFoundError:
        return None


def get_file_modified(path: os.PathLike | str) -> int | None:
    """Return the modified time as epoch time of path."""
    try:
        return round(Path(path).stat().st_mtime)
    except FileNotFoundError:
        return None


def get_file_size(path: os.PathLike | str) -> int | None:
    """Return the size of path."""
    try:
        return Path(path).stat().st_size
    except FileNotFoundError:
        return None


def get_human_args(args: Sequence[str] | str | bytes) -> str:
    """Return subprocess args to a human-friendly string"""
    if isinstance(args, (list, tuple)):
        return " ".join(shlex.quote(arg) for arg in args)
    elif isinstance(args, bytes):
        return args.decode("utf-8", errors="ignore")
    elif args is None:
        return ""
    else:
        return str(args)


def get_human_file_size(size: int, width: int = 3) -> str:
    """Return the file size as a human-friendly string."""
    return HumanNumberFormatter.format_number(size, width=width)


def get_human_time(timestamp: int) -> str:
    """Return the time epoch as a human-friendly string."""
    try:
        dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    except Exception:
        return f"XXXX-XX-XXTXX:XX:XXZ ({timestamp})"
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ") + f" ({timestamp})"


def get_user_cache_dir() -> Path:
    """
    Return the (hopefully platform-independent) cache directory for the
    current user.
    """

    if os.name == "nt":
        return (
            Path(os.environ.get("LOCALAPPDATA") or (Path.home() / "AppData" / "Local"))
            / __program__
            / "Cache"
        )
    else:  # posix
        return (
            Path(os.environ.get("XDG_CACHE_HOME") or (Path.home() / ".cache"))
            / __program__
        )


def parse_header_accept_ranges(headers: email.message.Message) -> bool:
    """Parse and return the Accept-Ranges header to determine server resume
    support."""
    return headers.get("accept-ranges") == "bytes"


def parse_header_content_length(headers: email.message.Message) -> int | None:
    """Parse and return the Content-Length header."""
    value = headers.get("content-length")
    if not isinstance(value, str):
        return None
    match = re.match(r"^\s*([0-9]+)\s*$", value)
    if match:
        return int(match[1])
    else:
        return None


def parse_header_content_md5(headers: email.message.Message) -> str | None:
    """Parse and return the Content-MD5 header as a hexdigest."""
    value = headers.get("content-md5")
    if not isinstance(value, str):
        return None
    try:
        raw = base64.b64decode(value)
    except ValueError:
        return None
    hex = raw.hex()
    return hex if len(hex) == 32 else None


def parse_header_etag(headers: email.message.Message) -> str | None:
    """Parse and return the ETag header."""
    value = headers.get("etag")
    if isinstance(value, str) and value:
        return value
    else:
        return None


def parse_header_last_modified(headers: email.message.Message) -> int | None:
    """Parse and return the Last-Modified header as epoch time."""
    value = headers.get("last-modified")
    if not isinstance(value, str):
        return None
    old_locale = locale.getlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_TIME, "C")
    try:
        dt = datetime.strptime(value, "%a, %d %b %Y %H:%M:%S GMT")
    except ValueError:
        return None
    finally:
        locale.setlocale(locale.LC_TIME, old_locale)
    dt = dt.replace(tzinfo=timezone.utc)
    return round(dt.timestamp())


def rm_f(path: os.PathLike | str) -> None:
    """Unlink path without complaining."""
    try:
        Path(path).unlink()
    except OSError:
        pass


def sanitize_filename(filename: str, os_name: str = "auto") -> str | None:
    """
    Return a filename that is likely sanitized for most operating systems.
    Return None if not possible.

    If os_name is 'auto', then use os.name.

    - Removes control-characters and /
    - Replaces < > : " | ? * \\ with _      (Windows-only)
    - Removes trailing . and spaces         (Windows-only)
    - Truncates filenames to 240 bytes in UTF-8

    https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names
    """
    if os_name == "auto":
        os_name = os.name
    filename = re.sub(r"[\x00-\x1F/]", "", filename)
    if os_name == "nt":
        filename = re.sub(r'[<>:"|?*\\]', "_", filename)
        filename = re.sub(r"[ .]+$", "", filename)
    truncated = filename.encode("utf-8", errors="ignore")[:240]
    filename = truncated.decode("utf-8", errors="ignore")
    filename = "" if filename in (".", "..") else filename
    return filename if filename else None


TXT = TypeVar("TXT", str, bytes)


def truncate(text: TXT, max: int = 80, ellipses: TXT | None = None) -> str | bytes:
    """
    Truncate the line to max characters.
    """
    if ellipses is None:
        if isinstance(text, bytes):
            ellipses = b"..."
        else:
            ellipses = "..."

    if len(text) > max and max >= 0:
        if len(ellipses) > max:
            text = ellipses[:max]
        else:
            text = text[: max - len(ellipses)] + ellipses  # type: ignore
    return text


def urllib_safe_url(url: str) -> str:
    """Convert a human-entered url into one acceptable by urllib."""
    if not url.startswith("/"):
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme == "" and parsed.netloc == "":
            return f"http://{url}"
    return url
