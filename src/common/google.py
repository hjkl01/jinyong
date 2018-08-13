#!/usr/bin/env python
# coding=utf-8

import requests

def googleproxy(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    print('crawling : %s' % url.encode('utf-8'))
    try:
        response = requests.get(url, headers=headers)
        print('status_code is %s' % response.status_code)
        return response.content
    except Exception as err:
        print(err)
        return None

if __name__ == '__main__':
    url = 'https://google.com'
    googleproxy(url)
