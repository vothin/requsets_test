# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: shop_seller.py
    @time: 2019/11/21 17:14
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Shop_Seller(Requests_Test):

    # 创建医生机构
    def post_shop_seller_shops_createHospital(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Shop', 'shop_seller_shops_createHospital')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



if __name__ == '__main__':
    s = Shop_Seller()



    result = s.post_shop_seller_shops_createHospital('16312345678', '123456')

    print(result)
    print(result)