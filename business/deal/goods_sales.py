# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_sales.py
    @time: 2019/11/11 10:09
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Goods_Sales(Requests_Test):

    # 查询某商品的销售记录
    def get_goods_sales(self, goods_id, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'goods_sales')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])
