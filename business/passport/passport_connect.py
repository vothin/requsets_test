# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_connect.py
    @time: 2019/11/20 12:07
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Passport_Connect(Requests_Test):

    # 检测openid是否绑定
    def get_passport_connect_openid(self, type, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   openid        openid
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_openid')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 获取app联合登录所需参数
    def get_passport_connect_appParm(self, type, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   type        登录类型,可用值:QQ,WEIBO,WECHAT,ALIPAY
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_appParm')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # APP获取支付宝登录授权SDK
    def get_passport_connect_loginBinder_info(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_loginBinder_info')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # app用户名密码登录绑定
    def post_passpost_connect_loginBinder_app(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   openid          第三方平的openid
                        type            登录方式，可选有：qq、weixin、weibo、alipay
                        username        用户名
                        password        密码
                        captcha         图片验证码
                        uuid            唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_loginBinder_app')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # app注册绑定api
    def post_passpost_connect_registerBinder_app(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   openid          第三方平的openid
                        type            登录方式，可选有：qq、weixin、weibo、alipay
                        username        用户名
                        password        密码
                        captcha         图片验证码
                        uuid            唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_registerBinder_app')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # app手机短信登录绑定
    def post_passpost_connect_smsBinder_app(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   sms_code        短信码
                        openid          第三方平的openid
                        type            登录方式，可选有：qq、weixin、weibo、alipay
                        username        用户名
                        password        密码
                        captcha         图片验证码
                        uuid            唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_smsBinder_app')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



if __name__ == '__main__':
    p = Passport_Connect()

    # result = p.get_passport_connect_openid('1', '13412345678', '123456')
    # result = p.get_passport_connect_appParm('QQ', '13412345678', '123456')
    result = p.get_passport_connect_loginBinder_info('13412345678', '123456')

    print(result)
    print(result.text)