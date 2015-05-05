======================
cookiecutter-pypackage
======================

Forked from `cookiecutter`_ template for a Python package. Forked from
`audreyr/cookiecutter-pypackage`_.

It is inspired by `flask`_ and `werkzeug`_'s project style patterns. It is
used on the `tmuxp`_, `cihai-python`_ and `vcspull`_ projects.

- Free software: BSD license
- Vanilla testing setup with `unittest` and `python setup.py test`
- Travis-CI_: Ready for Travis Continuous Integration testing
- Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3
- Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_. Note: You can install sphinx docs requirements with ``$ pip install -r docs/requirements.txt``.

Additions and changes
---------------------

Testing
~~~~~~~

- `flask`_/`werkzeug`_-style testsuites. See `werkzeug testsuite`_ on
  github.
- Use ``run-tests.py`` to run all tests, or pass in arguments to test a
  particular ``TestSuite``, ``TestCase`` or ``Test``:

  .. code-block:: bash

      $ ./run-tests.py
      $ ./run-tests.py yourpackage
      $ ./run-tests.py repo_name.repo_name  # package_name.TestSuite
      $ ./run-tests.py yourpackage.testsuite.test_something
      $ ./run-tests.py testsuite.test_something
      $ ./run-tests.py test_something
      $ ./run-tests.py test_something test_something_docstring

- ``setup.py`` downloads ``unittest2`` for python 2.6.

Python 2.7+3.3
~~~~~~~~~~~~~~

- .. code-block:: python

      from __future__ import absolute_import, division, print_function, \
          with_statement, unicode_literals
- ``repo_name/_compat.py`` module (derived from flask, werkzeug and
  jinja2.) Why a compatibility module? See Armin Ronacher's post `Porting
  to Python 3 Redux`_.

.. _Porting to Python 3 Redux: http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/

Packaging
~~~~~~~~~

- ``repo_name/__init__.py`` + ``repo_name/__about__.py``: Metadata in
  ``repo_name/__init__.py`` e.g. ``__title__``, ``__author__`` can be
  accessed via:

  .. code-block:: python

      >>> about = {}
      >>> with open("repo_name/__about__.py") as fp:
      >>>     exec(fp.read(), about)
      >>> print(about['__title__'])
      Your project name

  Keeps ``setup.py`` and ``doc/conf.py`` in sync with package metadata.
  pypi and readthedocs distributions build off the latest package data.

  This method avoids cost of tokenizing and importing python file and
  avoids encountering potential import errors that may arise. It simply
  opens a vanilla python file and evals it.

  Derived from `pypa/warehouse`_.

- Relative imports in ``repo_name/__init__.py``.
- Relative imports in ``repo_name/testsuite/__init__.py``.
- Relative imports in ``repo_name/testsuite/{{ cookiecutter.package_name }}.py``.

.. _pypa/warehouse: https://github.com/pypa/warehouse

Docs
~~~~

- ``README.rst`` reStructuredText table for project information.
- vim modelines for ``rst`` in ``TODO`` and ``CHANGELOG``.
- ``docs/requirements.txt``, which can be targetted to install `sphinx
  changelog`_ package on `ReadTheDocs`. It will also trigger `-r
  ../requirements.txt`.
- `sphinx changelog`_ module, (imitation of `sqlalchemy`_, see `sqlalchemy
  changelog`_)
- Add ``TODO`` and ``docs/roadmap.rst``.
- Rename ``CHANGELOG.rst`` -> ``CHANGELOG``.
- Add ``docs/api.rst`` for documentation of API code. Initial class
  imported with docstring example.
- Automatically generate header spacing based on length of
  ``cookiecutter`` variables.

Example data
~~~~~~~~~~~~

- Example TestCase.
- Example Class w/ docstrings.

.. _flask: http://flask.pocoo.org
.. _werkzeug: http://werkzeug.pocoo.org
.. _werkzeug testsuite: https://github.com/mitsuhiko/werkzeug/tree/master/werkzeug/testsuite
.. _sqlalchemy: http://sqlalchemy.org
.. _sqlalchemy changelog: http://docs.sqlalchemy.org/en/latest/changelog/ 
.. _sphinx changelog: https://pypi.python.org/pypi/changelog
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _How can I get the version defined in setup.py setuptools in my package?: http://stackoverflow.com/a/3619714

Usage
-----

Install `cookiecutter`_:

.. code-block:: bash

    $ sudo pip install cookiecutter

Generate a Python package project:

.. code-block:: bash

    $ cookiecutter https://github.com/tony/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your `Travis-CI`_ account.
* Add the repo to your `ReadTheDocs`_ account + turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: Original pypackage.
* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description. 

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
.. _tmuxp: https://github.com/tony/tmuxp
.. _vcspull: https://github.com/tony/vcspull
.. _cihai-python: https://github.com/cihai/cihai-python
