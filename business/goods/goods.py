#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: select_goods.py
    @time: 2019/10/31 14:18
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.recordlog import logs
from common.config import Config

class Goods(Requests_Test):

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



    # 查询商品
    def goods(self, goods_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods')

        url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)



    # 查询商品是否有货
    def goods_area(self, goods_id, area_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_area')

        url = self.url_joint(prod).format(goods_id, area_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)



    # 获取sku信息
    def goods_skus(self, goods_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_skus')

        url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)



    # 获取商品浏览次数
    def goods_visit(self, goods_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_visit')

        url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)


if __name__ == '__main__':
    g = Goods()
    # result = g.goods(1)
    # result = g.goods_area(345, 123129)
    # result = g.goods_skus(345)
    result = g.goods_visit(1)
    print(result.text)

