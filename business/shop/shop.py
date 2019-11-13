# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: shop.py
    @time: 2019/11/7 15:01
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs

class Shop(Requests_Test):

    # H5申请o2o店铺
    def post_o2o_shop_apply(self, username=None, password=None, data=None, prod=False):
        '''
           相关参数有：  shop_name            店铺名称
                       link_name            店铺联系人
                       link_phone           联系人手机
                       shop_add             店铺详细地址
                       bank_name            银行名称
                       bank_account_name    银行户名
                       bank_number          银行账号
                       shop_region          shop_region
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        # 生成url
        self.suffix = self.c.get_value('Shop', 'shop_o2o_apply')
        if gu[2]:
            self.url = self.url_joint(prod) + '?' + gu[2]
        else:
            self.url = self.url_joint(prod)

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])


if __name__ == '__main__':
    data = {
        'shop_name' :   'python_shop',
        'link_name' :   'python_name',
        'link_phone' :  'python_phone',
        'shop_add' :    'python_add',
        'bank_name' :   'python_bank',
        'bank_account_name' :   'python_account',
        'bank_number' : 'python_number',
        'shop_region' : '18,1482,48941'
    }
    s = Shop()
    result = s.post_o2o_shop_apply('16312345678', '123456', data)
    print(result)
    print(result.text)
    print(result.url)