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

    def post_nce_device_info_add(self, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Device', 'ncs_device_info_add')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)




if __name__ == '__main__':
    n = Ncs_Device()
    captcha = 'qn64'

    data = {
        # 'softVer' : 'S01',
        "code" : "2214",
        # 'name' : '%E6%8A%A4%E5%A3%AB%E4%B8%BB%E6%9C%BA',
        # 'model' : 'WD',
        # 'ethMac' : '1C%3A05%3A00%3A00%3A00%3A08',
        # 'hardVer' : 'HSI',
        # 'type' : '1'
    }

    result = n.post_nce_device_info_add('16312345678', '123456', data=data, prod=10)

    print(result)
    print(result.text)
    print(result.url)


