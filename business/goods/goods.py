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
from common.change_urls import Change_Urls

class Goods(Requests_Test):

    # 查询商品
    def get_goods(self, goods_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods')
        self.suffix = self.suffix.format(goods_id)

        cu = Change_Urls()
        # gu = cu.get_urls(suffix=self.suffix, username=username, password=password, prod=prod)
        gu = cu.get_urls(self.suffix, username, password, prod=prod)

        return self.get_requests(gu[0], gu[1])



    # 查询商品是否有货
    def get_goods_area(self, goods_id, area_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_area')
        self.suffix = self.suffix.format(goods_id, area_id)

        cu = Change_Urls()
        # gu = cu.get_urls(suffix=self.suffix, username=username, password=password, prod=prod)
        gu = cu.get_urls(self.suffix, username, password, prod=prod)

        return self.get_requests(gu[0], gu[1])



    # 获取sku信息
    def get_goods_skus(self, goods_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_skus')
        self.suffix = self.suffix.format(goods_id)

        cu = Change_Urls()
        # gu = cu.get_urls(suffix=self.suffix, username=username, password=password, prod=prod)
        gu = cu.get_urls(self.suffix, username, password, prod=prod)

        return self.get_requests(gu[0], gu[1])




    # 获取商品浏览次数
    def get_goods_visit(self, goods_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_visit')
        self.suffix = self.suffix.format(goods_id)

        cu = Change_Urls()
        # gu = cu.get_urls(suffix=self.suffix, username=username, password=password, prod=prod)
        gu = cu.get_urls(self.suffix, username, password, prod=prod)

        return self.get_requests(gu[0], gu[1])


if __name__ == '__main__':
    g = Goods()
    # result = g.get_goods(456)
    # result = g.get_goods(456, username='13412345678', password='123456')
    # result = g.get_goods_area(345, 123129)
    # result = g.get_goods_area(345, 123129, username='13412345678', password='123456')
    # result = g.get_goods_skus(345, prod=True)
    result = g.get_goods_skus(345, username='13412345678', password='123456', prod=True)
    # result = g.get_goods_visit(1, username='13412345678', password='123456')
    # result = g.get_goods_visit(1)
    # result2 = g.get_goods_visit(1, prod=True)
    print(result.text)
    # print(result2.text)

