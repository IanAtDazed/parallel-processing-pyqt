"""Modules containing NamedTuple classes."""

from typing import NamedTuple


class MessageSignal(NamedTuple):
    """Indicates a value is available for the view."""

    value: any
