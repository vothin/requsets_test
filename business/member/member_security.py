# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_security.py
    @time: 2019/11/20 10:52
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Security(Requests_Test):

    # 发送绑定手机验证码
    def post_member_security_bind_send(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid          uuid客户端的唯一标识
                        captcha       图片验证码
                        mobile        手机号码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_security_bind_send')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 手机号码绑定API
    def put_member_security_bind(self, moblie, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code        手机验证码
                        mobile          手机号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_security_bind')
        self.suffix = self.suffix.format(moblie)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 验证换绑验证验证码
    def get_member_security_exchange_bind(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code        手机验证码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_security_exchange_bind')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 手机号码换绑API
    def put_member_security_exchange_bind_mobile(self, moblie, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code        手机验证码
                        mobile          手机号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_exchange_bind_mobile')
        self.suffix = self.suffix.format(moblie)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 验证修改密码验证码
    def get_member_security_password(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code        手机验证码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_security_password')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改密码
    def put_member_security_password(self, moblie, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid            uuid客户端的唯一标识
                        captcha         图片验证码
                        password        密码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_security_password')
        self.suffix = self.suffix.format(moblie)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 发送手机验证验证码
    def post_member_security_send(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid          uuid客户端的唯一标识
                        captcha       图片验证码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_security_send')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)