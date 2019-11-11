# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: trade.py
    @time: 2019/11/11 14:42
    @desc:
'''
# ********************************************************



from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Trade(Requests_Test):


    # 创建交易
    def post_tarde_create(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  client          app下单使用，传值APP
        '''
        self.suffix = self.c.get_value('Deal', 'tarde_create')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])
