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
from common.change_param import Change_Param

class Goods(Requests_Test):

    # 查询商品
    def get_goods(self, goods_id, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Goods', 'goods')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)




    # 查询商品是否有货
    def get_goods_area(self, goods_id, area_id, username=None, password=None, data=None, prod=False):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Goods', 'goods_area')
        self.suffix = self.suffix.format(goods_id, area_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


    # 获取sku信息
    def get_goods_skus(self, goods_id, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Goods', 'goods_skus')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 获取商品浏览次数
    def get_goods_visit(self, goods_id, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Goods', 'goods_visit')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    g = Goods()
    # result = g.get_goods(456)
    # result = g.get_goods(456, '13412345678', '123456')
    # result = g.get_goods_area(345, 123129)
    # result = g.get_goods_area(345, 123129, username='13412345678', password='123456')
    # result = g.get_goods_skus(345, prod=True)
    # result = g.get_goods_skus(345)
    # result = g.get_goods_skus(345, '13412345678', '123456', prod=True)
    result = g.get_goods_skus(345, username='13412345678', password='123456', prod=False)
    # result = g.get_goods_visit(345, username='13412345678', password='123456')
    # result = g.get_goods_visit(1)
    # result2 = g.get_goods_visit(1, prod=True)
    print(result.text)
    # print(result.url)
    # print(result2.text)

