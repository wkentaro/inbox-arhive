#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {0}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {0}'.format(post_id)


if __name__ == '__main__':
    app.run()