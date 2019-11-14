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
        self.suffix = ''                                    # section参数
        self.url = ''                                       # url地址
        self.token = ''                                     # token参数
        self.uid = ''                                       # uid参数
        self.headers = None                                 # headers参数


    # # 初始化读取配置文件url.ini
    # def __init__(self, username=None, password=None):
    #     self.c = Config()
    #     self.prefix1 = self.c.get_value('URL', 'dev_url')   # 测试环境
    #     self.prefix2 = self.c.get_value('URL', 'url')       # 正式环境
    #     self.prefix3 = self.c.get_value('URL', '192_url')
    #     self.suffix = ''                                    # section参数
    #     self.url = ''                                       # url地址
    #     self.token = ''                                     # token参数
    #     self.uid = ''                                       # uid参数
    #     self.headers = None                                 # headers参数
    #
    #     self.uuid = '777'                                   # uuid参数
    #     self.timestamp = str(int(time.time()) * 1000)       # timestamp参数
    #     self.nonce = str(random.randint(100000, 999999))    # nonce参数
    #     self.sign = ''                                      # sign参数
    #     self.headers = {'uuid' : self.uuid}
    #     self.url_tail = ''
    #
    #     self.username = username                            # 登录账号
    #     self.password = password                            # 登录密码
    #     # self.data = None                                    # data参数
    #     # self.prod = False                                   # prod控制器



    # url拼接
    def url_joint(self, prod=False):
        if prod:
            self.url =  self.prefix2 + self.suffix          # 测试环境url
        else:
            self.url = self.prefix1 + self.suffix           # 正式环境url
            
        # self.url = self.prefix3 + self.suffix               # 本地环境url
        return self.url
