#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals
)


import sys
import os
import argparse

import kaptan
from flask import Flask

from . import exc
from ._compat import reraise
from .util import convert_to_attr_dict, merge_dict, import_string, \
    default_config


class {{ cookiecutter.repo_name | capitalize }}(object):
    """App factory."""

    def __init__(self, config):

        #: configuration dictionary. Available as attributes. ``.config.debug``
        self.config = convert_to_attr_dict(config)

        app = Flask(__name__)
        app.config.from_object(dict(self.config))

        # iterate through blueprints in config.
        for url_prefix, blueprint_str in self.config.blueprints.items():
            blueprint = import_string(blueprint_str)

            try:
                app.register_blueprint(blueprint, url_prefix=url_prefix)
            except AttributeError as e:
                type, value, traceback = sys.exc_info()
                raise reraise(exc.AppBlueprintLoadException, value, traceback)

        self.app = app

    def __call__(self):
        return self.app

    def run(self, host=None, port=None, debug=None, **options):
        """Pass-through to ``~.app`` object's :meth:`Flask.run()`. Mixes in
        ``port`` and ``host``."""

        port = self.config.get('port') or port
        host = self.config.get('host') or host
        debug = self.config.get('debug') or debug
        app_config = {(k, v) for k, v in self.config.items() if k in Flask.default_config.keys()}
        options = merge_dict(app_config, options)

        self.app.run(host, port, debug, **options)

    @classmethod
    def from_file(cls, config_path=None, *args, **kwargs):
        """Create a Flask app instance from a JSON or YAML config.
        :param config_path: path to custom config file
        :type confiig_path: str
        :rtype: :class:`{{ cookiecutter.repo_name | capitalize }}`
        """

        config = dict()
        configReader = kaptan.Kaptan()

        config = configReader.import_config(default_config).get()

        if config_path:
            if not os.path.exists(config_path):
                raise Exception('{0} does not exist.'.format(os.path.abspath(config_path)))
            if not any(config_path.endswith(ext) for ext in ('json', 'yml', 'yaml', 'ini')):
                raise Exception(
                    '{0} does not have a yaml,yml,json,ini extension.'
                    .format(os.path.abspath(config_path))
                )
            else:
                custom_config = configReader.import_config(config_path).get()
                config = merge_dict(config, custom_config)

        return cls(config)

    @classmethod
    def from_cli(cls, argv):
        """Flask application instance from :py:class:`argparse` / CLI args.
        :param argv: list of arguments, i.e. ``['-c', 'dev/config.yml']``.
        :type argv: list
        :rtype: :class:`{{ cookiecutter.repo_name | capitalize }}` with
            :class:`flask.Flask` on :prop:`self.app`.
        """
        parser = argparse.ArgumentParser(prog="git_pull")
        parser.add_argument("-c", "--config", dest="_config")

        args = parser.parse_args(argv)
        config = args._config if args._config is not None else None

        return cls.from_file(config)
