# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_register.py
    @time: 2019/11/20 18:19
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Passport_Register(Requests_Test):

    # 从维鼎康联删除用户
    def post_passport_deleteByUsername_fromWDKL(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username           username
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_deleteByUsername_fromWDKL')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 从WDKL同步登录 用户名（手机号）/密码登录API
    def post_passport_loginFromWDKL(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username            username
                        password            password
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginFromWDKL')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # app注册
    def post_passport_register_app(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid                客户端唯一标识
                        mobile              手机号
                        sms_code            手机验证码
                        uid
                        username            会员登陆用户名
                        nickname            真实姓名
                        password            密码
                        confirmpassword     确认密码
                        scope               执医类型
                        face
                        refreshToken
                        accessToken
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_register_app')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 从App常规注册用户
    def post_passport_register_app_normal(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile              手机号
                        username            会员登陆用户名
                        password            密码
                        isself              isself 是否本人：0无关 1本人 2亲朋
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_register_app_normal')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)