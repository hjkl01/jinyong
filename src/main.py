#!/usr/bin/env python
# encoding: utf-8

import os
from flask import Flask, render_template, jsonify, send_from_directory
from common.google import googleproxy
from common.crawler import _try
from common.model import Jinyong as jy
from common.dumblog import dlog
logger = dlog(__file__)
app = Flask(__name__)


@app.route('/')
def index():
    _str = '<html>  <meta http-equiv="refresh" content="0;url=./home/">  </html> '
    return _str


@app.route('/home/')
def home():
    return render_template('home.html')


@_try
@app.route('/ludingji/')
@app.route('/ludingji/<page>')
def ludingji(page=1):
    if int(page) > 52:
        result = 'page num is wrong !'
        return jsonify(result)
    qu = jy.select().where(jy.id == page).get()
    titles = [t.title for t in jy.select()]
    result = [x for x in qu.content.split('br')]
    return render_template('ludingji.html', content=result, head=qu.name, titles=titles, title=qu.title)


@app.route('/<path:_file>')
def favicon(_file):
    return send_from_directory(os.path.join(app.root_path, 'static'), _file)


@app.route('/google/<path:word>')
def google(word='python'):
    url = 'https://www.google.com.hk/search?hl=en&q=%s' % word
    return googleproxy(url)


@_try
@app.route('/v/')
def list_movies():
    import os
    files = os.listdir('video')
    return render_template('listdir.html', data=files)


@_try
@app.route('/v/<filename>')
def get_file(filename):
    path = 'video'
    return send_from_directory(path, filename)


#@_try
#@app.route('/secret/')
#def _srcret():
#    return render_template('secret.html')
#

@_try
@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
    # app.run()
