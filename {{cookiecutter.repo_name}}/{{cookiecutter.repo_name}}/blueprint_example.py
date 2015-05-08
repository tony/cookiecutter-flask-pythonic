# -*- coding: utf-8 -*-

"""Blueprint for JSON API."""

from __future__ import absolute_import, division, print_function, \
    with_statement, unicode_literals

from flask import Blueprint, request, jsonify

blueprint_example = Blueprint('blueprint_example', __name__)


@blueprint_example.route('/blueprint_example', defaults={'page': 'index'})
@blueprint_example.route('/<page>')
def show(page):
    return 'hi'


@blueprint_example.route('/test')
def say_something():
    question = request.args.get('question', type=str)

    response = {
        "this": question,
        "answer": "Always the same!"
    }

    return jsonify(response)
