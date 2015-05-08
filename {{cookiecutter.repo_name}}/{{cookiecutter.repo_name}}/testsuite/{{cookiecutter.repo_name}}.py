#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.repo_name }}` module."""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)

import os

from flask import json

from ..util import settings_path
from .. import {{ cookiecutter.repo_name }}
from . import unittest

test_config = os.path.join(settings_path, 'testing.yml')

class {{ cookiecutter.repo_name | capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def test_something_docstring(self):
        """Here is a sample test with a docstring. Hey."""
        self.assertTrue(True)

    def tearDown(self):
        pass


class BlueprintExample(unittest.TestCase):

    app = None

    def setUp(self):
        if not self.app:
            app = {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name|capitalize }}.from_file(test_config).app
            app.config['TESTING'] = True
            # Default port is 5000
            app.config['LIVESERVER_PORT'] = 8943
            self.app = app.test_client()
        return self.app

    def test_server_is_up(self):
        url = 'blueprint_example/test?q=${question}'.format(
            question="What's the meaning of life?"
        )
        response = self.app.get(url)
        self.assertNotEqual(response.status_code, 404)

    def test_response(self):
        url = 'blueprint_example/test?q=${question}'.format(
            question="What's the meaning of life?"
        )
        response = self.app.get(url)

        self.assertIsNotNone(response.data)
        data = json.loads(response.data)

        self.assertEqual(
            set(data.keys()),
            set(["answer", "this"])
        )


def suite():
    from .helpers import setup_path
    setup_path()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite({{ cookiecutter.repo_name | capitalize }}))
    suite.addTest(unittest.makeSuite(BlueprintExample))
    return suite
