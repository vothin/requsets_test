#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: config.py
    @time: 2019/10/31 10:35
    @desc:
'''
# ********************************************************

import configparser
from base.global_path import url_path
from common.recordlog import logs

class Config(object):

    def __init__(self):
        self.conf = self.get_url_config()

    # 读取配置文件url_path
    def get_url_config(self):
        conf_obj = configparser.ConfigParser()
        conf_obj.read(url_path, encoding='utf-8')
        return conf_obj

    # 获取配置文件的值
    def get_value(self, sec_name, opt_name):
        try:
            return self.conf.get(sec_name, opt_name)
        except Exception as e:
            logs.error(e)


if __name__ == '__main__':
    c = Config()
    result = c.get_value('Goods', 'goods')
    print(result)