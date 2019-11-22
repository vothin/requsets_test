# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_hostpital.py
    @time: 2019/11/22 11:06
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Care_Hostpital(Requests_Test):

    # 判断是否已绑定床位
    def get_care_hostpital(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_hostpital')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


if __name__ == '__main__':
    c = Care_Hostpital()

    result = c.get_care_hostpital('13412345678', '123456', prod=3)
    print(result)
    print(result.text)