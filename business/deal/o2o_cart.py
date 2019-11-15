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

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)




    # 清空o2o购物车
    def del_o2o_catrs_del(self, username=None, password=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_del')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 获取o2o购物车页面的购物情况
    def get_o2o_carts_all(self, username=None, password=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_all')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # o2o立即购买
    def post_o2o_carts_buy(self, username=None, password=None, data=None, prod=False):
        '''
                    相关参数有：  sku_id      产品ID            True
                                num         此产品的购买数量    True
                                activity    默认参与的活动id    False
                '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_buy')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 获取结算页面O2O购物车详情
    def get_o2o_carts_checked(self, username=None, password=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_checked')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 设置全部商为选中或不选中
    def post_o2o_carts_checked(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  checked     是否选中,可用值:0,1
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_checked')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


    # 批量设置某商家的商品为选中或不选中
    def post_o2o_carts_seller(self, seller_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  seller_id   卖家id
                        checked     是否选中,可用值:0,1
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_seller')
        self.suffix = self.suffix.format(seller_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


    # 更新O2O购物车中的多个产品
    def post_o2o_carts_sku(self, sku_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_id      产品id
                        checked     是否选中,可用值:0,1
                        num         产品数量
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_sku')
        self.suffix = self.suffix.format(sku_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 删除O2O购物车中的一个或多个产品
    def del_o2o_carts_sku(self, sku_ids, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_ids     	产品id，多个产品可以用英文逗号：(,) 隔开
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'o2o_carts_sku_del')
        self.suffix = self.suffix.format(sku_ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



if __name__ == '__main__':
    data = {
        'sku_id' : '596',
        'num' : '1'
    }

    checked = {'checked' : '0'}

    num  = {'num' : '9'}

    c = O2O_Cart()
    # result = c.post_o2o_catrs('13412345678', '123456', data)
    result = c.get_o2o_carts_all('13412345678', '123456')
    # result = c.del_o2o_catrs_del('13412345678', '123456')
    # result = c.get_o2o_carts_checked('13412345678', '123456')
    # result = c.post_o2o_carts_buy('13412345678', '123456', data)
    # result = c.post_o2o_carts_checked('13412345678', '123456', checked)
    # result = c.post_o2o_carts_seller('26', '13412345678', '123456', checked)
    # result = c.post_o2o_carts_sku('597', '13412345678', '123456', num)
    # result = c.del_o2o_carts_sku('597,596', '13412345678', '123456')
    print(result)
    print(result.text)



