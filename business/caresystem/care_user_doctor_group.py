# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_user_doctor_group.py
    @time: 2019/11/22 11:46
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_User_Doctor_Group(Requests_Test):


    # 添加医生用户分组
    def post_care_user_doctor_group(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_group')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 删除医生用户分组
    def del_care_user_doctor_group(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_group_id')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个医生用户分组
    def get_care_user_doctor_group(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_group_id')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改医生用户分组
    def put_care_user_doctor_group(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_group_id')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_User_Doctor_Group()

    data = {
        'create_member_id' : '4473',
        'group_name' : 'chuangjianfenzu',

    }

    # result = c.post_care_user_doctor_group('16312345678', '123456', data=data)
    # result = c.get_care_user_doctor_group('146', '16312345678', '123456')
    # result = c.put_care_user_doctor_group('146', '16312345678', '123456', data=data)
    result = c.del_care_user_doctor_group('146', '16312345678', '123456')
    print(result)
    print(result.text)




