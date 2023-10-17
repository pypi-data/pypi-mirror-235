#
# File:    ./tests/unit/test_version.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2023-10-15 11:07:49 +0200
# Project: tmug: Make developer's life easier
#
# SPDX-License-Identifier: MIT
#
"""Test :mod:`tmug.version` module."""

from vutils.testing.testcase import TestCase

from tmug.version import __version__


class VersionTestCase(TestCase):
    """Test case for version."""

    __slots__ = ()

    def test_version(self):
        """Test if version is defined properly."""
        self.assertIsInstance(__version__, str)
