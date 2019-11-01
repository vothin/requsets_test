#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: requests.py
    @time: 2019/10/30 16:31
    @desc:
'''
# ********************************************************

import requests
from base.base import Base
from common.recordlog import logs
from common.config import Config

class Requests_Test(Base):

    # get请求
    def get_requests(self, url):
        r = requests.get(url)
        return r

    # post请求
    def post_requests(self, url, postdata):
        r = requests.post(url, data=postdata)
        return r



if __name__ == '__main__':
    r = Requests_Test()
    # r.get_requests('http://dev.buyer.wdklian.com/goods/345')


