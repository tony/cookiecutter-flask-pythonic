#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

{{ cookiecutter.project_name }}
{{ '-' * cookiecutter.project_name|count }}

{{ cookiecutter.project_short_description }}

"""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

import os

current_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
))
parent_path = os.path.dirname(current_path)
settings_path = os.path.join(parent_path, 'settings')
default_config = os.path.join(settings_path, 'default.yml')

from .{{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name | capitalize }}
