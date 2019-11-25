#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from flask_script import Manager

from {{ cookiecutter.repo_name }} import {{ cookiecutter.repo_name | capitalize }}

"""If not using Flask-Script::

app = {{ cookiecutter.repo_name | capitalize }}.from_cli(sys.argv[1:])

Does the trick for retrieving an application object using
pure argparse. But let's hook into Flask-Script's CLI argparse
instance.
"""


def app_wrapper(*args, **kwargs):
    """App factory returns the :class:`flask.Flask` via ``__call__``,
    but because of the way :class:`flask_script.Manager` handles
    accepting app objects, this wrapper returns the flask object directly.

    :returns: Flask object build from CLI
    :rtype: :class:`flask.Flask`

    """

    return {{ cookiecutter.repo_name | capitalize }}.from_file(*args, **kwargs).app

manager = Manager(app_wrapper)
manager.add_option('-c', '--config', dest='config', required=False)


@manager.command
def run_server(*args, **kwargs):
    {{ cookiecutter.repo_name | capitalize }}.from_file().run()


@manager.command
def testing(*args, **kwargs):
    print('Run "./run-tests.py" or "python setup.py test".')

if __name__ == "__main__":
    run_server()
