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
from common.get_headers import Get_Headers

class Goods(Requests_Test):

    # 查询商品
    def url_goods(self, goods_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods')

        if username != None:
            gh = Get_Headers(username, password)
            sh = gh.set_headers()
            self.headers = sh[0]
            url = self.url_joint(prod).format(goods_id) + sh[1]

        else:
            url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url, headers=self.headers)



    # 查询商品是否有货
    def url_goods_area(self, goods_id, area_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_area')

        if username != None:
            gh = Get_Headers(username, password)
            sh = gh.set_headers()
            self.headers = sh[0]
            url = self.url_joint(prod).format(goods_id, area_id) + sh[1]

        else:
            url = self.url_joint(prod).format(goods_id, area_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url, headers=self.headers)



    # 获取sku信息
    def url_goods_skus(self, goods_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_skus')

        if username != None:
            gh = Get_Headers(username, password)
            sh = gh.set_headers()
            self.headers = sh[0]
            url = self.url_joint(prod).format(goods_id) + sh[1]

        else:
            url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url, headers=self.headers)


    # 获取商品浏览次数
    def url_goods_visit(self, goods_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_visit')

        if username != None:
            gh = Get_Headers(username, password)
            sh = gh.set_headers()
            self.headers = sh[0]
            url = self.url_joint(prod).format(goods_id) + sh[1]

        else:
            url = self.url_joint(prod).format(goods_id)

        logs.info('Test interface:%s' % url)
        return self.get_requests(url, headers=self.headers)


if __name__ == '__main__':
    g = Goods()
    # result = g.url_goods(456)
    # result = g.url_goods(456, username='13412345678', password='123456')
    # result = g.url_goods_area(345, 123129)
    # result = g.url_goods_area(345, 123129, username='13412345678', password='123456')
    # result = g.url_goods_skus(345, prod=True)
    # result = g.url_goods_skus(345, username='13412345678', password='123456', prod=True)
    # result = g.url_goods_visit(1, username='13412345678', password='123456')
    result = g.url_goods_visit(1)
    # result2 = g.url_goods_visit(1, prod=True)
    print(result.text)
    # print(result2.text)

