"""Module containing process instruction NamedTuple classes.

**Note:** NamedTuple classes were chosen because:
- If futher instructions are required, they can include additional argument fields.
- NamedTuple (as opposed to namedtuple) classes allow for docstrings.
"""

from typing import NamedTuple


class QuitProcessing(NamedTuple):
    """Indicates that processing should quit."""

    pass
