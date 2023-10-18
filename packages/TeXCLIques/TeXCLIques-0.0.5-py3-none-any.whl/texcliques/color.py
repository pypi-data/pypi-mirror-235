from __future__ import annotations

from texcliques.constants import COLORS


def colored_message(msg: str, color: str, end: str = 'normal') -> str:
    """Color the background and text of a message."""
    end = COLORS.get(end, COLORS['normal'])
    return f"{color}{msg}{end}"


def step(
    message: str,
    *,
    start: str = '',
    color: str = 'normal',
    cols: int = 80,
) -> None:
    """Print a message with a colored background and text."""
    color = COLORS.get(color, COLORS['normal'])
    message = colored_message(message, color)
    dots = "." * (cols - len(start) - len(message) + len(color))
    print(f"{start}{dots}{message}", end=None)
