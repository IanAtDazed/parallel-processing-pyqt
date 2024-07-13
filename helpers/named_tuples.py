"""Modules containing NamedTuple classes."""

from typing import NamedTuple


class UpdateSignal(NamedTuple):
    """Indicates a value is available for the view."""

    value: int
