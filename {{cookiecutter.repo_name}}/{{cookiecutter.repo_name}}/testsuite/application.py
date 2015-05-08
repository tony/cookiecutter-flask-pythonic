#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Application object."""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)

import os

from ..util import settings_path
from .. import {{ cookiecutter.repo_name }}, exc
from . import unittest

test_config = os.path.join(settings_path, 'testing.yml')

class Application(unittest.TestCase):

    def test_registering_module_object_raises_helpful_exception(self):
        """Raises more helpful exception in case of http://stackoverflow.com/q/26550180."""
        config = {
            "blueprints": {
                "/": "{{ cookiecutter.repo_name }}.core"
            }
        }

        with self.assertRaises(exc.AppBlueprintLoadException):
            app = {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name|capitalize }}(config).app


def suite():
    from .helpers import setup_path
    setup_path()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Application))
    return suite
