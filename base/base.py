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
from common.config import Config

class Base():

    # 初始化读取配置文件url.ini
    def __init__(self):
        self.c = Config()
        self.prefix1 = self.c.get_value('URL', 'dev_url')
        self.prefix2 = self.c.get_value('URL', 'url')
        self.suffix = ''
        self.url = ''

    # url拼接
    def url_joint(self, prod=False):
        if prod:
            self.url =  self.prefix2 + self.suffix
        else:
            self.url = self.prefix1 + self.suffix
        return self.url
