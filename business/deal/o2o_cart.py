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

    def url_o2o_catrs(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  sku_id      产品ID            True
                        num         此产品的购买数量    True
                        activity    默认参与的活动id    False
        '''

        self.suffix = self.c.get_value('Deal', 'o2o_carts')

        cu = Change_Urls()
        gu = cu.get_urls(self.suffix, username, password, prod=prod)

        return self.post_requests(gu[0], gu[1], data)



if __name__ == '__main__':
    data = {
        'sku_id'    : 1,
        'num'       : 1
    }

    c = O2O_Cart()
    result = c.url_o2o_catrs(data=data)

    print(result)
    print(result.text)



