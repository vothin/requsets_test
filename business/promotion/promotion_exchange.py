# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: promotion_exchange.py
    @time: 2019/11/21 14:44
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Promotion_Exchange(Requests_Test):

    # 查询积分分类集合
    def get_promotions_exchange_cats(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_exchange_cats')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询积分商品
    def get_promotions_exchange_goods(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_exchange_goods')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    p = Promotion_Exchange()

    # result = p.get_promotions_exchange_cats()
    result = p.get_promotions_exchange_goods()
    print(result)
    print(result.text)