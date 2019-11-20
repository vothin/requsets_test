# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_login.py
    @time: 2019/11/20 16:52
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Passport_Login(Requests_Test):

    # APP登陆Wap用户信息验证
    def get_passport_apploginvild(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uid                 用户Id
                        access_token        传递的授权access_token
                        refresh_token       传递的refresh_token
                        uuid                客户端唯一标识
                        accessToken         accessToken
                        refreshToken        refreshToken
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_apploginvild')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 用户名（手机号）/密码登录API
    def get_passport_login(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username            用户名
                        password            密码
                        captcha             验证码
                        uuid                客户端唯一标识
                        platform            用户登陆平台(android|ios)
                        devicetoken         用户设备对应推送APP的token
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_login')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 发送验证码
    def post_passport_login_smscode(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid            uuid客户端的唯一标识
                        captcha         图片验证码
                        mobile          手机号码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_login_smscode')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 手机号码登录API
    def get_passport_login_mobile(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code            手机验证码
                        uuid                客户端唯一标识
                        mobile              手机号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_login_mobile')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # sns用户名（手机号）/密码登录API
    def get_passport_loginForSns(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username            用户名
                        password            密码
                        captcha             验证码
                        uuid                客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginForSns')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # sns用户名（手机号）/密码登录API(不用图形验证码)
    def get_passport_loginForSnsWithoutCode(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username            用户名
                        password            密码
                        uuid                客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginForSnsWithoutCode')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 登录及注册发送验证码(无图形验证码)
    def post_passport_loginOrRegister_smscode(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile     手机号码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginOrRegister_smscode')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 手机号码登录API传Dvicetoken
    def get_passport_loginWithDevicetoken(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code            手机验证码
                        mobile              手机号
                        uuid                客户端唯一标识
                        platform            用户登陆平台(android|ios)
                        devicetoken         用户设备对应推送APP的token
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginWithDevicetoken')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 手机号码登录及注册API(无图形验证码)
    def post_passport_loginOrRegister_noCaptcha(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile              手机号码
                        sms_code            手机验证码
                        uuid                客户端唯一标识
                        platform            用户登陆平台(android|ios)
                        devicetoken         用户设备对应推送APP的token
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginOrRegister_noCaptcha')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 用户名（手机号）/密码登录API
    def get_passport_nocaptchalogin(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uid                 用户ID
                        cuuid               客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_nocaptchalogin')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)