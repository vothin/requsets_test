# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: shop_clerks.py
    @time: 2020/1/3 14:40
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs

class Shop_Clerk(Requests_Test):

    # 查看店员详细信息
    def get_shop_clerk_getDetail(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  shopId          店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Shop', 'shop_clerk_getDetail')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


if __name__ == '__main__':
    s = Shop_Clerk()

    result = s.get_shop_clerk_getDetail('16412345678', '123456', prod=5)

    print(result)
    print(result.text)