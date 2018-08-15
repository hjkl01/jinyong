# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from lxml.etree import HTML
import gevent
from common.dumblog import dlog#, multi, crawler, save
from common.crawler import crawler, save, multi
from common.model import Jinyong

logger = dlog(__file__, console='debug')


class spider(object):

    @staticmethod
    @save
    def crawl(url, _id):
        logger.info('%s %s' % (url, _id))
        rep = crawler(url)
        html = HTML(rep.text)
        item = {}
        item['url'] = url
        item['id'] = _id
        item['name'] = html.xpath(r'//*[@id="breadnav"]/a[2]//text()')[-1]
        item['title'] = html.xpath(r'//*[@id="title"]//text()')[-1]
        pre_content = html.xpath(r'//*[@id="vcon"]//p//text()')
        item['content'] = ''
        for con in pre_content:
            item['content'] += con.strip() + 'br'
        #logger.info('title is %s' % item.get('title'))
        return item

def before_run():
    import os
    dirs = os.listdir()
    if 'settings.yaml' not in dirs:
        _config = '''User-Agent : Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36\ncookie : \ntime_sleep : 2 '''
        with open('settings.yaml', 'w') as file:
            file.write(_config)
    else:
        logger.info('settings.yaml is existed')


def run():
    _func = spider().crawl
    jobs = [gevent.spawn(_func, 'http://www.jinyongwang.com/lu/%s.html'%i, i-821) for i in range(822, 874)]
    gevent.joinall(jobs) 
    logger.info('mission finished !')


if __name__ == "__main__":
    try:
        Jinyong.create_table()
    except Exception as err:
        logger.info(err)
    before_run()
    run()
