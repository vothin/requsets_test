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

    # 根据店铺id获取店铺信息
    def get_shop_getByShopId(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  shopId          店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Shop', 'shop_getByShopId')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询店铺所有医生
    def get_shop_getDoctorListByShopId(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  shopId          店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Shop', 'shop_getDoctorListByShopId')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 获取店铺+店铺详情信息(未登录状态)
    def get_shop_getShopAndDetailInfo_id(self, id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  shopId          店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Shop', 'shop_getShopAndDetailInfo_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)





    # H5申请o2o店铺
    def post_o2o_shop_apply(self, username=None, password=None, data=None, prod=None):
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
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Shop', 'shop_o2o_apply')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



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

    shop_id = {'shopId' : '19'}

    get_data = {
        'shopId' : '347'
    }

    s = Shop()
    # result = s.get_shop_getByShopId('13412345678', '123456', get_data, prod=2)
    # result = s.post_o2o_shop_apply('16312345678', '123456', data)
    # result = s.get_shop_getDoctorListByShopId('13412345678', '123456', shop_id)
    # result = s.get_shop_getDoctorListByShopId(data=shop_id)
    result = s.get_shop_getShopAndDetailInfo_id('19', '13412345678', '123456', prod=2)
    print(result)
    print(result.text)
    print(result.url)