from __future__ import unicode_literals

import os
import sys
import termstyle

import pip

from cookiecutter.main import cookiecutter

from sniffer.api import file_validator, runnable

project_name = "boilerplate"
extra_context = {
    "project_name": project_name,
    "repo_name": project_name,
}

current_dir = cookiecutter_dir = os.path.dirname(os.path.abspath(__file__))


# you can customize the pass/fail colors like this
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

# All lists in this variable will be under surveillance for changes.
watch_paths = ['{{cookiecutter.repo_name}}/']

@file_validator
def py_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.') and filename != ".tmuxp"


from contextlib import contextmanager
import tempfile
import shutil

@contextmanager
def TemporaryDirectory(*args, **kwargs):
    _file = tempfile.mkdtemp(*args, **kwargs)
    try:
        yield _file
    finally:
        shutil.rmtree(_file)


@runnable
def execute_nose(*args):
    with TemporaryDirectory() as temp_dir:
        try:
            boilerplate = None
            project_dir = os.path.join(temp_dir, project_name)
            requirements = os.path.join(project_dir, 'requirements.txt')

            cookiecutter(
                cookiecutter_dir, no_input=True, extra_context=extra_context,
                output_dir=temp_dir
            )

            if project_dir not in sys.path:
                sys.path.append(project_dir)

            try:
                import boilerplate

                from boilerplate.testsuite import main
            except ImportError:
                pip.main(['install', '-r', requirements])
                import boilerplate

                from boilerplate.testsuite import main

            return main()
        except SystemExit as x:
            if hasattr(x, 'message'):
                print("Found error {0}: {1}".format(x.code, x.message))
                return not x.code
            else:
                return 1
