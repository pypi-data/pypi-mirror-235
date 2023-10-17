#
# File:    ./src/tmug/main.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2023-10-15 11:07:49 +0200
# Project: tmug: Make developer's life easier
#
# SPDX-License-Identifier: MIT
#
"""Application entry point definition."""

import sys
from typing import Callable, List, Optional


def main(argv: Optional[List[str]] = None) -> int:
    """Run tmug."""
    argv = argv or sys.argv
    # Your code goes here
    return 0


def start(
    name: str,
    exit_func: Callable[[int], None] = sys.exit,
    main_func: Callable[[Optional[List[str]]], int] = main,
    args: Optional[List[str]] = None,
) -> None:
    """Start the application."""
    if name == "__main__":
        exit_func(main_func(args))


start(__name__)
