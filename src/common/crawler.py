# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from functools import wraps
import multiprocessing
import requests
from flask import render_template
from .pipeline import Setting
from .model import Jinyong
from .dumblog import dlog
logger = dlog(__file__)


def crawler(url):
    headers = {
        'Cookie': Setting.Cookie,
        'User-Agent': Setting.UserAgent,
    }
    logger.info('crawling : %s' % (url))
    try:
        response = requests.get(url, headers=headers)
        logger.info('status_code is %s' % response.status_code)
        time.sleep(Setting.time_sleep)
        # return response.content
        return response
    except Exception as err:
        print(err)
        return None


def filter(lis, word=''):
    if len(lis) == 0:
        return ''
    elif len(lis) == 1:
        if lis[0] == '':
            return ''
        else:
            return lis[0].strip()
    elif len(lis) > 1:
        return word.join(lis).replace('  ', '').replace('\r', '').replace('\n', '').strip()


def save(fun):
    def wrap(*args):
        try:
            item = fun(*args)
            # item = ast.literal_eval(item)
            Jinyong.create(
                id=item['id'],
                title=item['title'],
                name=item['name'],
                url=item['url'],
                content=item['content'],
            )
            logger.info('saved success %s' % item['title'])
            #logger.info('saved success %s' % item['title'].encode('utf-8', 'ignore'))
        except Exception as err:
            logger.error(err)

    return wrap


def _try(func):
    @wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as err:
            print(err)
            return render_template('404.html')

    return wrapper



def multi(func, *_args):
    p = multiprocessing.Process(target=func, args=_args)
    p.start()
    import time
    time.sleep(Setting.time_sleep)
    logger.info('process start ! func :: %s, args :: %s' % (func.__name__, _args))


# def _gevent(func, _args=None):
#     if _args:
#         jobs = [gevent.spawn(func, arg) for arg in _args]
#     else:
#         jobs = [gevent.spawn(func,)]
#     result = gevent.joinall(jobs)
#     return result
