# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from lxml.etree import HTML
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


def run():
    for i in range(822, 874):
        _id = i - 821
        url = 'http://www.jinyongwang.com/lu/%s.html' % i
        multi(spider().crawl, url, _id)
        time.sleep(2)
        #break
    logger.info('mission finished !')


if __name__ == "__main__":
    try:
        Jinyong.create_table()
    except Exception as err:
        logger.info(err)
    run()
