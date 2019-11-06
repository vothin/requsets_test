# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: o2o_cart.py
    @time: 2019/11/5 16:34
    @desc:
'''
# ********************************************************

import requests
from common.recordlog import logs
from common.requests_test import Requests_Test
from common.change_param import Change_Param

class O2O_Cart(Requests_Test):

    # 向o2o购物车添加商品
    def post_o2o_catrs(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_id      产品ID            True
                        num         此产品的购买数量    True
                        activity    默认参与的活动id    False
        '''

        self.suffix = self.c.get_value('Deal', 'o2o_carts')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 清空o2o购物车
    def del_o2o_catrs_del(self, username=None, password=None, prod=False):

        self.suffix = self.c.get_value('Deal', 'o2o_carts_del')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0])



    # 获取o2o购物车页面的购物情况
    def get_o2o_carts_all(self, username=None, password=None, prod=False):

        self.suffix = self.c.get_value('Deal', 'o2o_carts_all')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # o2o立即购买
    def post_o2o_carts_buy(self, username=None, password=None, data=None, prod=False):
        '''
                    相关参数有：  sku_id      产品ID            True
                                num         此产品的购买数量    True
                                activity    默认参与的活动id    False
                '''

        self.suffix = self.c.get_value('Deal', 'o2o_carts_buy')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 获取结算页面O2O购物车详情
    def get_o2o_carts_checked(self, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'o2o_carts_checked')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 设置全部商为选中或不选中
    def post_o2o_carts_checked(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  checked     是否选中,可用值:0,1
        '''
        self.suffix = self.c.get_value('Deal', 'o2o_carts_checked')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 批量设置某商家的商品为选中或不选中






if __name__ == '__main__':
    data = {
        'sku_id' : '501',
        'num' : '1'
    }

    c = O2O_Cart()
    result = c.post_o2o_catrs('13412345678', '123456', data, prod=True)
    # result = c.get_o2o_carts_all('13412345678', '123456')
    # result = c.del_o2o_catrs_del('13412345678', '123456')
    # result = c.get_o2o_carts_checked('13412345678', '123456')
    print(result)
    print(result.text)



