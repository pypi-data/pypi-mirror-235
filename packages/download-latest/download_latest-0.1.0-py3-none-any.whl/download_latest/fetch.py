from __future__ import annotations

import http.client
import io
import os
import logging
import shutil
import socket
from typing import Any, ClassVar, List, Tuple, Type
import urllib.parse
import urllib.request

from .meta import DEFAULT_LOGGER
from .task import SubProcessTask, Task, TaskUncaughtError
from .util import get_human_args, truncate, urllib_safe_url

__all__ = [
    "DEFAULT_CURL_PATH",
    "DEFAULT_FETCH_BACKEND",
    "FETCH_BACKENDS",
    "Fetch",
    "FetchCurl",
    "FetchCurlDownloadTask",
    "FetchCurlHeadTask",
    "FetchException",
    "FetchMeter",
    "FetchParseException",
    "FetchPython",
    "FetchPythonDownloadTask",
    "FetchPythonHeadTask",
    "FetchResponse",
]

DEFAULT_CURL_PATH: str = "curl"
DEFAULT_FETCH_BACKEND: str = "auto"
FETCH_BACKENDS: list[str] = ["auto", "curl", "python"]


class FetchException(http.client.HTTPException):
    """Exception from Fetch."""

    pass


class FetchParseException(FetchException):
    """HTTP parse exception from Fetch."""

    pass


class FetchMeter:
    """
    An abstract class that can be used with Fetch to provide a progress meter.
    """

    def period(self) -> float | int:
        """Return the time in seconds per iteration."""
        return 0.1

    def begin(
        self,
        path: os.PathLike | str | None = None,
        remote_size: int | None = None,
    ) -> None:
        """Called at the beginning of the loop."""
        pass

    def step(self, index: int) -> None:
        """
        Called with each loop iteration.

        The index argument will provide a running count, starting at 0.
        """
        pass

    def end(self) -> None:
        """Called at the end of the loop."""
        pass


class FetchResponse:
    """A useful subset of an HTTPResponse."""

    def __init__(
        self,
        url: str,
        headers: http.client.HTTPMessage,
        status: int,
        reason: str,
    ):
        self.url = url
        self.headers = headers
        self.status = status
        self.reason = reason

    @classmethod
    def make_from_http_response(
        cls, response: http.client.HTTPResponse
    ) -> FetchResponse:
        return cls(
            url=response.url,  # type: ignore
            headers=response.headers,
            status=response.status,
            reason=response.reason,
        )

    @classmethod
    def make_from_raw_headers(cls, url: str, raw_headers: bytes) -> FetchResponse:
        """
        The HTTPResponse initializer patched to support bytes instead of a
        socket argument.
        """

        class FakeSocket(socket.socket):
            def __init__(self, fp: io.IOBase) -> None:
                self.fp = fp

            def makefile(self, *args, **kwargs) -> io.IOBase:  # type: ignore
                return self.fp

        raw_headers = cls._patch_raw_headers(raw_headers)
        raw_stream = io.BytesIO(raw_headers)
        sock = FakeSocket(raw_stream)

        try:
            response = http.client.HTTPResponse(sock, method="HEAD", url=url)
            response.begin()
        except (http.client.HTTPException, ValueError):
            raise FetchParseException("cannot parse response")

        return cls(
            url=url,
            headers=response.headers,
            status=response.status,
            reason=response.reason,
        )

    @classmethod
    def make_from_raw_multiple_headers(
        cls,
        url: str,
        raw_multiple_headers: bytes,
    ) -> list[FetchResponse]:
        """
        Return a list of FetchResponses from the raw bytes of one or more HEAD
        requests.
        """
        responses = []
        for raw_headers in raw_multiple_headers.strip().split(b"\r\n\r\n"):
            response = cls.make_from_raw_headers(url=url, raw_headers=raw_headers)
            responses.append(response)
            location = response.headers["location"]
            if location:
                url = urllib.parse.urljoin(url, location)
        return responses

    @classmethod
    def _patch_raw_headers(cls, raw_headers: bytes) -> bytes:
        """
        Replace HTTP/x with HTTP/1.1 in a raw response so HTTPResponse.begin()
        doesn't throw an exception. Also, add a fake HTTP status line if we
        don't find one to handle non-HTTP protocols.
        """
        raw_lines = raw_headers.strip().split(b"\r\n")
        parts = raw_lines[0].split(None, 1) if raw_lines else []
        if parts and parts[0].startswith(b"HTTP"):
            raw_lines[0] = b" ".join([b"HTTP/1.1"] + parts[1:])
        else:
            raw_lines.insert(0, b"HTTP/1.1 200 OK")
        return b"\r\n".join(raw_lines + [])


class Fetch:
    """Abstract HTTP request / response handler."""

    logger: logging.Logger
    meter: FetchMeter | None

    def __init__(
        self,
        logger: logging.Logger | None = None,
        meter: FetchMeter | None = None,
    ) -> None:
        """
        Create a Fetch instance.
        """
        self.logger = DEFAULT_LOGGER if logger is None else logger
        self.meter = meter

    def download(
        self,
        url: str,
        path: os.PathLike | str,
        remote_size: int | None = None,
        resume: bool = False,
    ) -> bool:
        """
        Download url to path and return success.
        """
        raise NotImplementedError()

    def head(self, url: str) -> list[FetchResponse]:
        """
        Make HEAD requests to url and return the responses.
        """
        raise NotImplementedError()

    def run_task(
        self,
        task: Task[Any],
        path: os.PathLike | str | None = None,
        remote_size: int | None = None,
    ) -> None:
        """
        Run the task with the meter.
        """
        if not self.meter:
            task.wait()
            return

        self.meter.begin(path=path, remote_size=remote_size)
        for index in task.loop(period=self.meter.period()):
            self.meter.step(index)
        self.meter.end()

    @staticmethod
    def get_fetch_class(backend: str) -> Type[FetchCurl] | Type[FetchPython]:
        if backend == "auto":
            if shutil.which(DEFAULT_CURL_PATH):
                return FetchCurl
            else:
                return FetchPython
        elif backend == "curl":
            return FetchCurl
        else:
            return FetchPython


class FetchCurl(Fetch):
    """cURL HTTP request / response handler."""

    MAX_STDOUT_STDERR_LENGTH: ClassVar[int] = 50

    def download(
        self,
        url: str,
        path: os.PathLike | str,
        remote_size: int | None = None,
        resume: bool = False,
    ) -> bool:
        """
        Download url to path and return success.
        """
        task = FetchCurlDownloadTask(url=url, path=path, resume=resume)
        self._log_begin(task)
        try:
            self.run_task(task, path=path, remote_size=remote_size)
        except TaskUncaughtError as e:
            self._log_error(repr(e.error))
            return False
        finally:
            self._log_end(task)

        return self._check_process(task)

    def head(self, url: str) -> list[FetchResponse]:
        """
        Make HEAD requests to url and return the responses.
        """
        task = FetchCurlHeadTask(url=url)

        self._log_begin(task)
        try:
            self.run_task(task)
        except TaskUncaughtError as e:
            self._log_error(repr(e.error))
            return []
        finally:
            self._log_end(task)

        if not self._check_process(task):
            return []

        try:
            return FetchResponse.make_from_raw_multiple_headers(
                url=url, raw_multiple_headers=task.get().stdout
            )
        except FetchParseException as e:
            self._log_error(repr(e))
            return []

    # Private

    def _check_process(self, task: SubProcessTask) -> bool:
        process = task.get()
        if process.returncode == 0:
            return True
        else:
            if process.stderr:
                msg = (
                    process.stderr.split(b"\n")[0]
                    .decode("utf-8", errors="ignore")
                    .strip()
                )
            else:
                msg = f"curl exited {process.returncode}"
            self.logger.error(f"    curl: {msg}")
            return False

    def _log_begin(self, task: SubProcessTask) -> None:
        self.logger.debug(f"    curl: $ {get_human_args(task.args)}")

    def _log_end(self, task: SubProcessTask) -> None:
        try:
            process = task.get()
        except Exception:
            self.logger.debug("    curl: code=? out=? err=?")
            return

        code, out, err = process.returncode, process.stdout, process.stderr
        maxlen = self.MAX_STDOUT_STDERR_LENGTH
        if len(out) + len(err) > maxlen:
            # prefer stderr over stdout
            if len(err) < maxlen:
                out = truncate(out, maxlen - len(err))
            else:
                out = b"..."
            if len(out) + len(err) > maxlen:
                err = truncate(err, maxlen - 3)

        self.logger.debug(f"    curl: code={code} out={out!r} err={err!r}")

    def _log_error(self, msg: str) -> None:
        self.logger.error(f"    curl: error: {msg}")


class FetchCurlDownloadTask(SubProcessTask):
    """Download using cURL."""

    def __init__(
        self,
        url: str,
        path: os.PathLike | str,
        resume: bool,
    ):
        args = [
            DEFAULT_CURL_PATH,
            "--silent",
            "--show-error",
            "--fail",
            "--location",
            "--output",
            str(path),
            *(["--continue-at", "-"] if resume else []),
            "--",
            url,
        ]
        super().__init__(args=args)
        self.url = url
        self.path = path
        self.resume = resume


class FetchCurlHeadTask(SubProcessTask):
    """Make HEAD requests using cURL."""

    def __init__(self, url: str):
        args = [
            DEFAULT_CURL_PATH,
            "--silent",
            "--show-error",
            "--location",
            "--head",
            "--",
            url,
        ]
        super().__init__(args=args)
        self.url = url


class FetchPython(Fetch):
    """Python HTTP request / response handler."""

    def download(
        self,
        url: str,
        path: os.PathLike | str,
        remote_size: int | None = None,
        resume: bool = False,
    ) -> bool:
        """
        Download url to path and return success.
        """
        task = FetchPythonDownloadTask(url=url, path=path, resume=resume)

        self._log_begin(f"download {url} -> {str(path)}")
        try:
            self.run_task(task, path=path, remote_size=remote_size)
            return True
        except TaskUncaughtError as e:
            self._log_error(repr(e.error))
            return False
        finally:
            self._log_end("download finished")

    def head(self, url: str) -> list[FetchResponse]:
        """
        Make HEAD requests to url and return the responses.
        """
        task = FetchPythonHeadTask(url=url)

        self._log_begin(f"head {url}")
        try:
            self.run_task(task)
        except TaskUncaughtError as e:
            self._log_error(repr(e.error))
            return []
        finally:
            self._log_end("head finished")

        responses = list(map(FetchResponse.make_from_http_response, task.get()))
        if responses:
            return responses
        else:
            self._log_error("no response received")
            return []

    # Private

    def _log_begin(self, msg: str) -> None:
        self.logger.debug(f"  python: {msg}")

    def _log_end(self, msg: str) -> None:
        self.logger.debug(f"  python: {msg}")

    def _log_error(self, msg: str) -> None:
        self.logger.error(f"  python: error: {msg}")


class FetchPythonDownloadTask(Task[Tuple[str, http.client.HTTPMessage]]):
    """Download using Python urllib.request."""

    def __init__(
        self,
        url: str,
        path: os.PathLike | str,
        resume: bool,
    ):
        """
        Create the download task.
        """
        super().__init__()
        self.url = url
        self.path = path
        self.resume = resume

    def run(self) -> tuple[str, http.client.HTTPMessage]:
        """
        Run the download task.
        """
        request_url = urllib_safe_url(self.url)
        return urllib.request.urlretrieve(request_url, filename=self.path)


class FetchPythonHeadTask(Task[List[http.client.HTTPResponse]]):
    """Make HEAD requests using Python urllib.request."""

    def __init__(self, url: str) -> None:
        """
        Create the head task.
        """
        super().__init__()
        self.url = url

    def run(self) -> list[http.client.HTTPResponse]:
        """
        Run the head task.
        """
        url = self.url
        request_url = urllib_safe_url(url)
        responses: list[http.client.HTTPResponse] = []

        # append each redirect response to responses
        class RedirectHandler(urllib.request.HTTPRedirectHandler):
            def redirect_request(
                self, *args, **kwargs
            ) -> urllib.request.Request | None:
                fp: http.client.HTTPResponse = args[1]

                # ensure the first response url matches the user request
                if not responses:
                    fp.url = url  # type: ignore

                responses.append(fp)
                return super().redirect_request(*args, **kwargs)

        try:
            opener = urllib.request.build_opener(RedirectHandler)
            request = urllib.request.Request(request_url, method="HEAD")
            try:
                response = opener.open(request)
            except urllib.error.HTTPError as e:
                response = e.fp
            responses.append(response)

        finally:
            return responses
