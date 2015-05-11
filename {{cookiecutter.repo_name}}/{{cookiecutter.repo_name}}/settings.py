# -*- coding: utf-8 -*-

import os

current_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
))
parent_path = os.path.dirname(current_path)
settings_path = os.path.join(parent_path, 'settings')
default_config = os.path.join(settings_path, 'default.yml')
