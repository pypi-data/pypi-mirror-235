from __future__ import annotations

import math


class Spinner:
    r"""
    A simple spinner.

    >>> spinner = Spinner(chars="/-\\|", width=15, index=3)
    >>> for i, s in enumerate(spinner):
    ...    if i >= 6:
    ...        break
    ...    else:
    ...        print(s)
    ...
    /-\|/-\|/-\|/-\
    -\|/-\|/-\|/-\|
    \|/-\|/-\|/-\|/
    |/-\|/-\|/-\|/-
    /-\|/-\|/-\|/-\
    -\|/-\|/-\|/-\|
    """

    def __init__(
        self,
        chars: str = "/-\\|",
        width: int = 4,
        step: int = 1,
        index: int = 0,
    ) -> None:
        """Create the spinner."""
        self.chars = chars
        self.width = width
        self.step = step
        self.index = index % len(chars)

    def __iter__(self) -> Spinner:
        """Return the iterator (self)."""
        return self

    def __next__(self) -> str:
        """Return the next iteration of the spinner."""
        self.index = (self.index + self.step) % len(self.chars)
        # index, width = self.index, self.width
        chars = self.chars * (math.ceil((2 * self.width) / len(self.chars)))
        result = chars[self.index : self.index + self.width]
        return result
