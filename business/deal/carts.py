# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: carts.py
    @time: 2019/11/8 10:10
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Carts(Requests_Test):

    # 向购物车中添加一个产品
    def post_catrs(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_id      产品ID            True
                        num         此产品的购买数量    True
                        activity    默认参与的活动id    False
        '''

        self.suffix = self.c.get_value('Deal', 'carts')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 清空购物车
    def del_catrs_del(self, username=None, password=None, prod=False):

        self.suffix = self.c.get_value('Deal', 'carts_del')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0])



    # 获取购物车页面购物车详情
    def get_carts_all(self, username=None, password=None, prod=False):

        self.suffix = self.c.get_value('Deal', 'carts_all')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 立即购买
    def post_carts_buy(self, username=None, password=None, data=None, prod=False):
        '''
                    相关参数有：  sku_id      产品ID            True
                                num         此产品的购买数量    True
                                activity    默认参与的活动id    False
                '''

        self.suffix = self.c.get_value('Deal', 'carts_buy')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 获取结算页面购物车详情
    def get_carts_checked(self, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'carts_checked')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 设置全部商为选中或不选中
    def post_carts_checked(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  checked     是否选中,可用值:0,1
        '''
        self.suffix = self.c.get_value('Deal', 'carts_checked')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 批量设置某商家的商品为选中或不选中
    def post_carts_seller(self, seller_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  seller_id   卖家id
                        checked     是否选中,可用值:0,1
        '''
        self.suffix = self.c.get_value('Deal', 'carts_seller')
        self.suffix = self.suffix.format(seller_id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 更新O2O购物车中的多个产品
    def post_carts_sku(self, sku_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_id      产品id
                        checked     是否选中,可用值:0,1
                        num         产品数量
        '''
        self.suffix = self.c.get_value('Deal', 'carts_sku')
        self.suffix = self.suffix.format(sku_id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 删除O2O购物车中的一个或多个产品
    def del_carts_sku(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_ids     产品id，多个产品可以用英文逗号：(,) 隔开
        '''
        self.suffix = self.c.get_value('Deal', 'carts_sku_del')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0])




if __name__ == '__main__':
    c = Carts()
    result = c.get_carts_all('13412345678', '123456')
    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)
