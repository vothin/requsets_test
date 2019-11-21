# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: promotion_groupbuy.py
    @time: 2019/11/21 16:28
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Promotion_Groupbuy(Requests_Test):

    # 查询团购活动的信息
    def get_promotions_groupbuy_active(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_groupbuy_active')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)