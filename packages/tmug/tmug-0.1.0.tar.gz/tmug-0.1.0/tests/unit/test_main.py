#
# File:    ./tests/unit/test_main.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2023-10-15 11:07:49 +0200
# Project: tmug: Make developer's life easier
#
# SPDX-License-Identifier: MIT
#
"""
Test :mod:`tmug.main` module.

.. |__main__| replace:: :mod:`tmug.__main__`
.. |main| replace:: :func:`~tmug.main.main`
.. |start| replace:: :func:`~tmug.main.start`
"""

import importlib

from vutils.testing.mock import make_callable
from vutils.testing.testcase import TestCase

from tmug.main import main, start


class MainTestCase(TestCase):
    """Test case for entry points."""

    __slots__ = ("__main_args", "__main_returns")

    def setUp(self):
        """Set up the test."""
        self.__main_args = ["--foo", "--bar", "quux"]
        self.__main_returns = 42

    def test_main_module(self):
        """Test that |__main__| can be imported."""
        module = importlib.import_module("tmug.__main__")
        self.assertIsNotNone(module)
        self.assertTrue(hasattr(module, "__name__"))
        self.assertEqual(module.__name__, "tmug.__main__")

    def test_main_function(self):
        """Test that |main| returns zero."""
        self.assertEqual(main([]), 0)

    def test_start_function_import_case(self):
        """Test that |start| function do nothing during module import."""
        exit_func = make_callable()
        main_func = make_callable()
        start("foo", exit_func, main_func, self.__main_args)
        self.assert_not_called(main_func)
        self.assert_not_called(exit_func)

    def test_start_function_script_case(self):
        """Test that |start| function runs |main| during script invocation."""
        exit_func = make_callable()
        main_func = make_callable(self.__main_returns)
        start("__main__", exit_func, main_func, self.__main_args)
        self.assert_called_with(main_func, self.__main_args)
        self.assert_called_with(exit_func, self.__main_returns)
