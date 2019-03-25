#!/usr/bin/env python
# encoding: utf-8

import os
from flask import Flask, render_template, jsonify, send_from_directory
from common.model import Jinyong as jy
from loguru import logger
logger.add("logs/%s.log" % __file__.rstrip('.py'), format="{time:MM-DD HH:mm:ss} {level} {message}")
app = Flask(__name__)


@app.route('/')
def index():
    _str = '<html>  <meta http-equiv="refresh" content="0;url=http://www.xvim.top/home/">  </html> '
    return _str


@app.route('/home/')
def home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


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


@app.route('/google/')
def google():
    return render_template('google.html')


@app.route('/v/')
def list_movies():
    import os
    files = os.listdir('video')
    return render_template('listdir.html', data=files)


@app.route('/v/<filename>')
def get_file(filename):
    path = 'video'
    return send_from_directory(path, filename)


@app.route('/secret/')
def _srcret():
    return render_template('secret.html')


@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
    # app.run()
