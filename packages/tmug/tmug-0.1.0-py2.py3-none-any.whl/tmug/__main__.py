#
# File:    ./src/tmug/__main__.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2023-10-15 11:07:49 +0200
# Project: tmug: Make developer's life easier
#
# SPDX-License-Identifier: MIT
#
"""Enable invoking tmug by ``python -m tmug``."""

from tmug.main import start

start(__name__)
