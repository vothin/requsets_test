# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_nurse_config.py
    @time: 2020/1/3 17:31
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Care_Nurse_Config(Requests_Test):

    # 添加护理配置
    def post_care_employee(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_employee')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)
