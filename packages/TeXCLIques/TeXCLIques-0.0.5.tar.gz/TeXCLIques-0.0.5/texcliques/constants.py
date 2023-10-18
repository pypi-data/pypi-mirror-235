from __future__ import annotations

import os
import pathlib
from importlib import metadata

VERSION = metadata.version('TeXCLIques')
COMMANDS = ('extract-citations',)

COLORS = {
    'red': '\033[41m',
    'green': '\033[42m',
    'yellow': '\033[43;30m',
    'turquoise': '\033[46;30m',
    'subtle': '\033[2m',
    'normal': '\033[m'
}

DESCRIPTION = """\
TeXCLIques is a collection of utilities for working with scientific LaTeX files.

The following commands are available:
    - `extract-citations`: Extract the citations from a LaTeX file given a BIB
    file and save them in various formats.
"""

CWD = pathlib.Path(os.getcwd())
