{{ '=' * cookiecutter.project_name|count }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|count }}


.. image:: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.png?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.png
    :target: http://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/badge.png?branch=master
    :target: https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}?branch=master

.. image:: https://pypip.in/d/{{ cookiecutter.repo_name }}/badge.png
        :target: https://crate.io/packages/{{ cookiecutter.repo_name }}?version=latest

``{{ cookiecutter.repo_name }}`` - {{ cookiecutter.project_short_description }}

Features
--------

* TODO

==============  ==========================================================
Python support  Python 2.7, >= 3.3
Source          https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
Docs            http://{{ cookiecutter.repo_name }}.rtfd.org
Changelog       http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/history.html
API             http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/api.html
Issues          https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues
Travis          http://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
Test coverage   https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
pypi            https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}
Ohloh           https://www.ohloh.net/p/{{ cookiecutter.repo_name }}
License         `BSD`_.
git repo        .. code-block:: bash

                    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
install dev     .. code-block:: bash

                    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git {{ cookiecutter.repo_name }}
                    $ cd ./{{ cookiecutter.repo_name }}
                    $ virtualenv .env
                    $ source .env/bin/activate
                    $ pip install -e .
tests           .. code-block:: bash

                    $ python setup.py test
==============  ==========================================================

.. _BSD: http://opensource.org/licenses/BSD-3-Clause
.. _Documentation: http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/
.. _API: http://{{ cookiecutter.repo_name }}.readthedocs.org/en/latest/api.html
