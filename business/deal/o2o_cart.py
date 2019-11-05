# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: o2o_cart.py
    @time: 2019/11/5 16:34
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_urls import Change_Urls

class O2O_Cart(Requests_Test):

    def post_o2o_catrs(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_id      产品ID            True
                        num         此产品的购买数量    True
                        activity    默认参与的活动id    False
        '''

        self.suffix = self.c.get_value('Deal', 'o2o_carts')

        cu = Change_Urls()
        gu = cu.get_urls(self.suffix, username, password, data, prod=prod)

        return self.post_requests(gu[0], data, gu[1])



if __name__ == '__main__':
    data = {
        'sku_id' : 345,
        'num' : 1
    }

    c = O2O_Cart()
    result = c.post_o2o_catrs('13412345678', '123456', data)

    print(result)
    print(result.text)



