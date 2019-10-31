#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: select_goods.py
    @time: 2019/10/31 14:32
    @desc:
'''
# ********************************************************

import json
from business.goods.goods import Goods
from common.recordlog import logs


class Select_goods(Goods):

    def dev_select_goods(self, goods_id):
        logs.info('要查询的商品：%s' % goods_id)
        result = self.dev_goods(goods_id)
        print(result.text)


    def select_goods(self, goods_id):
        logs.info('要查询的商品：%s' % goods_id)
        result = self.goods(goods_id)
        print(result.text)

if __name__ == '__main__':
    s = Select_goods()
    s.dev_select_goods(354)
    s.select_goods(345)