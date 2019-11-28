# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_user_doctor_mapping.py
    @time: 2019/11/27 17:25
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_User_Doctor_Mapping(Requests_Test):

    # 查询一个用户的所有绑定医生机构
    def get_care_user_doctor_mapping(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_mapping')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 医生获取等待通过绑定列表
    def get_care_user_doctor_mapping_getWaitBindedList(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_mapping_getWaitBindedList')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_User_Doctor_Mapping()

    get_data = {
        'doctorId' : '56',
        'shopId' : '19'
    }

    # result = c.get_care_user_doctor_mapping('13412345678', '123456')
    result = c.get_care_user_doctor_mapping_getWaitBindedList('16312345678', '123456', get_data, prod=5)

    print(result)
    print(result.text)
