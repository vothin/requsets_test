# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_categories.py
    @time: 2019/10/31 18:23
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.recordlog import logs
from common.config import Config

class Goods_Categories(Requests_Test):

    # 初始化读取配置文件url.ini
    def __init__(self):
        self.c = Config()
        self.prefix1 = self.c.get_value('URL', 'dev_url')
        self.prefix2 = self.c.get_value('URL', 'url')
        self.suffix = ''

    # url拼接
    def url_joint(self, prod=False):
        if prod:
            url =  self.prefix2 + self.suffix
        else:
            url = self.prefix1 + self.suffix
        return url


    # 首页等商品分类数据
    def goods_categories(self, parent_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_categories')

        url = self.url_joint(prod).format(parent_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)


if __name__ == '__main__':
    g = Goods_Categories()
    result = g.goods_categories(2)
    print(result.text)