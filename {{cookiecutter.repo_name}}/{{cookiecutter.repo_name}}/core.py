# -*- coding: utf-8 -*-

"""Root application."""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

from flask import Blueprint, render_template_string

core = Blueprint('core', __name__)


@core.route('/', defaults={'page': 'index'})
def show(page):
    """Borrowed from DEFAULT_URLCONF_TEMPLATE, Django 1.8, License BSD."""

    {% raw %}
    WELCOME_TPL = """
    <!DOCTYPE html>
    <html lang="en"><head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="robots" content="NONE,NOARCHIVE"><title>{{ title }}</title>
    <style type="text/css">
        html * { padding:0; margin:0; }
        body * { padding:10px 20px; }
        body * * { padding:0; }
        body { font:small sans-serif; }
        body>div { border-bottom:1px solid #ddd; }
        h1 { font-weight:normal; }
        h2 { margin-bottom:.8em; }
        h2 span { font-size:80%; color:#666; font-weight:normal; }
        h3 { margin:1em 0 .5em 0; }
        h4 { margin:0 0 .5em 0; font-weight: normal; }
        table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
        tbody td, tbody th { vertical-align:top; padding:2px 3px; }
        thead th {
        padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
        font-weight:normal; font-size:11px; border:1px solid #ddd;
        }
        tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
        #summary { background: #e0ebff; }
        #summary h2 { font-weight: normal; color: #666; }
        #explanation { background:#eee; }
        #instructions { background:#f6f6f6; }
        #summary table { border:none; background:transparent; }
    </style>
    </head>
    <body>
    <div id="summary">
    <h1>{{ heading }}</h1>
    <h2>{{ subheading }}</h2>
    </div>
    <div id="instructions">
      {{ instructions }}
    <p>
    </p>
    </div>
    <div id="explanation">
      {{ explanation }}
    <p>
    </p>
    </div>
    </body></html>
    """
    {% endraw %}

    return render_template_string(
        WELCOME_TPL,
        heading="You've made it!",
        title="You've made it!",
        subheading="A modular flask experience.",
        instructions="Check out "
            "<a href='http://www.git-pull.com' target=_blank>git-pull.com</a> "
            "for instructions, updates and more pythonic, golang, saas "
            "and POSIX goodness. Daily reminder: <p />"
            "<pre>import this</pre> "
            "\"<em>C is truth.</em>\"",
        explanation = "You are a winner, and the chosen one."
    )
