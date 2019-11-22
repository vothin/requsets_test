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
        self.prefix1 = self.c.get_value('URL', 'dev_url')   # 测试环境
        self.prefix2 = self.c.get_value('URL', 'url')       # 正式环境
        self.prefix3 = self.c.get_value('URL', '192_url')
        self.prefix4 = self.c.get_value('URL', 'dev_seller_url')
        self.prefix5 = self.c.get_value('URL', 'seller_url')
        self.prefix6 = self.c.get_value('URL', '192_seller_url')
        self.suffix = ''                                    # section参数
        self.url = ''                                       # url地址
        self.token = ''                                     # token参数
        self.uid = ''                                       # uid参数
        self.headers = None                                 # headers参数



    # url拼接
    def url_joint(self, prod=None):
        if prod == None:
            self.url =  self.prefix1 + self.suffix          # 用户端测试环境url
        elif prod == 2:
            self.url = self.prefix2 + self.suffix           # 用户端正式环境url
        elif prod == 3:
            self.url = self.prefix3 + self.suffix           # 用户端本地环境url

        elif prod == 4:
            self.url = self.prefix4 + self.suffix           # 医生端测试环境url
        elif prod == 5:
            self.url = self.prefix5 + self.suffix           # 医生端正式环境url
        elif prod == 6:
            self.url = self.prefix6 + self.suffix           # 医生端本地环境url

        return self.url
