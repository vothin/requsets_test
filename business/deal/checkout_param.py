# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: checkout_param.py
    @time: 2019/11/8 11:11
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Checkout_Param(Requests_Test):

    # 获取结算参数
    def get_checkout_params(self, username=None, password=None, prod=False):

        self.suffix = self.c.get_value('Deal', 'checkout_params')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])

