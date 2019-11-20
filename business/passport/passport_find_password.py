# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_find_password.py
    @time: 2019/11/20 16:35
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Passport_Find_Password(Requests_Test):

    # 获取账户信息
    def get_passport_findPwd(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid         uuid客户端的唯一标识
                        captcha      图片验证码
                        account      账户名称
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_findPwd')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 发送验证码
    def post_passport_findPwd_send(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid            uuid客户端的唯一标识
                        captcha         验证码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_findPwd_send')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 修改密码
    def put_passport_findPWD_updatePWD(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   password        密码
                        uuid            客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_findPWD_updatePWD')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 验证找回密码验证码
    def get_passport_findPwd_valid(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid         uuid客户端的唯一标识
                        sms_code     验证码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_findPwd_valid')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)