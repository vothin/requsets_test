# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: promotion_coupon.py
    @time: 2019/11/21 14:29
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Promotion_Coupon(Requests_Test):

    # 查询商家优惠券列表
    def get_promotions_coupons(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_coupons')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询所有优惠券
    def get_promotions_coupons_all(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_coupons_all')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    p = Promotion_Coupon()

    # result = p.get_promotions_coupons('13412345678', '123456')
    result = p.get_promotions_coupons_all('13412345678', '123456')
    print(result)
    print(result.text)
