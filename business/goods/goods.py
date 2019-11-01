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

class URL_Goods(Requests_Test):

    # 查询商品
    def url_goods(self, goods_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods')

        url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)



    # 查询商品是否有货
    def url_goods_area(self, goods_id, area_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_area')

        url = self.url_joint(prod).format(goods_id, area_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)



    # 获取sku信息
    def url_goods_skus(self, goods_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_skus')

        url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)



    # 获取商品浏览次数
    def url_goods_visit(self, goods_id, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_visit')

        url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url)


if __name__ == '__main__':
    g = URL_Goods()
    # result = g.url_goods(1)
    # result = g.url_goods_area(345, 123129)
    # result = g.url_goods_skus(345, prod=True)
    result = g.url_goods_visit(1)
    result2 = g.url_goods_visit(1, prod=True)
    print(result.text)
    print(result2.text)

