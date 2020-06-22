# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_user_doctor_message.py
    @time: 2019/11/27 17:14
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Care_User_Doctor_Message(Requests_Test):

    # 添加留言
    def post_care_user_doctor_message_insert(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_message_insert')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询用户与医生的留言列表
    def post_care_user_doctor_message_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_doctor_message_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



if __name__ == '__main__':
    c = Care_User_Doctor_Message()

    post_data = {
        'page_no' : '1',
        'page_size' : '10',
        'doctorid' : '4473'
    }

    # result = c.post_care_user_doctor_message_insert('13412345678', '123456')
    result = c.post_care_user_doctor_message_page('13412345678', '123456', post_data)

    print(result)
    print(result.text)