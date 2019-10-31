#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: base.py
    @time: 2019/10/31 9:40
    @desc:
'''
# ********************************************************

import time, random, hashlib

class Base():

    def url_prod(self, url, prod=False):
        if prod:
            url= url
            # url += "?uid=" + self.uid +"&timestamp=" + self.timestamp +"&nonce="+ self.nonce + "&sign=" + self.sign
        else:
            url = url
        return url