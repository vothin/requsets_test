# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: ncs_device.py
    @time: 2019/12/10 15:27
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Ncs_Device(Requests_Test):

    # 获取店铺信息
    def get_ncs_shops_getShopDetail(self, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Device', 'ncs_shops_getShopDetail')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 根据父级id和店铺类型查询下级店铺
    def get_ncs_shops_getShopPageByParentId(self, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Device', 'ncs_shops_getShopPageByParentId')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)




    def post_ncs_device_info_add(self, username=None, password=None, data=None, prod=None, json=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Device', 'ncs_device_info_add')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)




if __name__ == '__main__':
    n = Ncs_Device()
    captcha = 'qn64'

    data = {
        'softVer' : 'S01',
        "code" : "2214",
        'name' : '%E6%8A%A4%E5%A3%AB%E4%B8%BB%E6%9C%BA',
        'model' : 'WD',
        'ethMac' : '1C%3A05%3A00%3A00%3A00%3A08',
        'hardVer' : 'HSI',
        'type' : '1'
    }

    get_data = {
        'page_no' : '1',
        'page_size' : '10',
        'shopType' : 5,
        'parentId' : '19'
    }

    get_data2 = {
        'shopId' : '19'
    }

    # result = n.post_ncs_device_info_add('16312345678', '123456', data, prod=10)
    # result = n.get_ncs_shops_getShopPageByParentId('16312345678', '123456', data, prod=10)
    result = n.get_ncs_shops_getShopDetail('13412345678', '123456', get_data2, prod=12)

    print(result)
    print(result.text)
    print(result.url)


