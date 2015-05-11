# -*- coding: utf-8 -*-
"""Exceptions."""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

from ._compat import text_type


APP_BLUEPRINT_LOAD_EXCEPTION_MSG = """
   You were not registering a Flask blueprint! Are you sure you've fully
   specified the *blueprint object* and not just the python module?

   Assuming foo_module.py or foo_module/__init__.py

   and the_blueprint = Blueprint('foo', __name__)

   ``foo_module`` is a module, that's not a blueprint object.
   ``foo_module.the_blueprint`` would be the blueprint!

   http://stackoverflow.com/q/26550180
"""

class AppException(Exception):

    """Base Exception for App Errors."""


class AppBlueprintLoadException(AppException):

    def __str__(self):
        return text_type(self.message) + APP_BLUEPRINT_LOAD_EXCEPTION_MSG
