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

import json
import requests
from base.base import Base
from common.recordlog import logs
from common.config import Config

class Requests_Test(Base):

    def requests_alt(self):
        return requests

    # get请求
    def get_requests(self, url, headers=None, get_data=None):
        self.headers = headers
        r = requests.get(url, headers=self.headers, params=get_data)
        return r



    # post请求
    def post_requests(self, url, headers=None, post_data=None):
        self.headers = headers

        r = requests.post(url, headers=self.headers, data=post_data)
        return r



    # delete请求
    def del_requests(self, url, headers=None):
        self.headers = headers
        r = requests.delete(url, headers=self.headers)



if __name__ == '__main__':
    r = Requests_Test()
    data = {'seller_id' : '16'}
    # data = '16'
    # result = r.get_requests('http://dev.buyer.wdklian.com/trade/carts/o2o/all')
    result = r.get_requests('http://dev.buyer.wdklian.com/goods/345/area/123129')
    # result = r.post_requests('http://dev.buyer.wdklian.com/trade/carts/o2o/seller/0', data)
    print(result)
    print(result.text)


