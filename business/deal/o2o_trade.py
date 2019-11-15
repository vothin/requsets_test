# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: o2o_trade.py
    @time: 2019/11/7 10:27
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.requests_test import Requests_Test
from common.change_param import Change_Param

class O2O_Trade(Requests_Test):

    # 创建O2O交易
    def post_o2o_trade_create(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  client      appO2O下单使用，传值APP
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_trade_create')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


if __name__ == '__main__':
    o = O2O_Trade()
    result = o.post_o2o_trade_create('13412345678', '123456')
    print(result)
    print(result.text)


