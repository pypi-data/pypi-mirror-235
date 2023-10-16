from __future__ import annotations

from re import sub

from utilities.typing import never

from .platform import SYSTEM  # noqa: TID252
from .platform import System  # noqa: TID252


def maybe_sub_pct_y(text: str, /) -> str:
    """Substitute the `%Y' token with '%4Y' if necessary."""
    if SYSTEM is System.windows:  # pragma: os-ne-windows
        return text
    if SYSTEM is System.mac_os:  # pragma: os-ne-macos
        return text
    if SYSTEM is System.linux:  # pragma: os-ne-linux
        return sub("%Y", "%4Y", text)
    return never(SYSTEM)  # pragma: no cover
