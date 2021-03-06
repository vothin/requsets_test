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
    def post_catrs(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  sku_id      产品ID            True
                        num         此产品的购买数量    True
                        activity    默认参与的活动id    False
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 清空购物车
    def del_catrs_del(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_del')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)




    # 获取购物车页面购物车详情
    def get_carts_all(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_all')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 立即购买
    def post_carts_buy(self, username=None, password=None, data=None, prod=None):
        '''
                    相关参数有：  sku_id      产品ID            True
                                num         此产品的购买数量    True
                                activity    默认参与的活动id    False
                '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_buy')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 获取结算页面购物车详情
    def get_carts_checked(self, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_checked')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)




    # 设置全部商为选中或不选中
    def post_carts_checked(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  checked     是否选中,可用值:0,1
        '''
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_checked')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 批量设置某商家的商品为选中或不选中
    def post_carts_seller(self, seller_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  seller_id   卖家id
                        checked     是否选中,可用值:0,1
        '''
        # 调用Change_Param类# 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_seller')
        self.suffix = self.suffix.format(seller_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


    # 更新购物车中的单个产品
    def post_carts_sku(self, sku_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  sku_id      产品id
                        checked     是否选中,可用值:0,1
                        num         产品数量
        '''
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_seller')
        self.suffix = self.c.get_value('Deal', 'carts_sku')
        self.suffix = self.suffix.format(sku_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 删除购物车中的一个或多个产品
    def del_carts_sku(self, sku_ids, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  sku_ids     产品id，多个产品可以用英文逗号：(,) 隔开
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'carts_sku_del')
        self.suffix = self.suffix.format(sku_ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)




if __name__ == '__main__':
    c = Carts()

    data = {
        'sku_id' : '600',
        'num' : '1'
    }

    data1 = {
        'checked' : '1'
    }

    data2 = {
        'checked' : '0'
    }

    data3 = {
        'num' : '3'
    }

    a = 591,592

    # result = c.post_catrs('13412345678', '123456', data)
    result = c.get_carts_all('13412345678', '123456')
    # result = c.del_catrs_del('13412345678', '123456')
    # result = c.post_carts_buy('13412345678', '123456', data)
    # result = c.get_carts_checked('13412345678', '123456', data)
    # result = c.post_carts_checked('13412345678', '123456', data1)
    # result = c.post_carts_seller('20', '13412345678', '123456', data2)
    # result = c.post_carts_sku('572', '13412345678', '123456', data3)
    # result = c.post_carts_sku('571', '13412345678', '123456', data3)
    # result = c.del_carts_sku('599,600', '13412345678', '123456')
    print(result)
    print(result.text)
    print(result.url)

