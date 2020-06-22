# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_connect.py
    @time: 2019/11/20 15:04
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Passport_Connect(Requests_Test):

    # 会员中心账号绑定回调地址
    def get_passport_accountBinder_callback(self, type, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   type        登录类型,可用值:QQ,WEIBO,WECHAT,ALIPAY
                        uid         会员id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_accountBinder_callback')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # PC发起信任登录
    def get_passport_connect_pc(self, type, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   type        登录类型,可用值:QQ,WEIBO,WECHAT,ALIPAY
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_pc')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # WAP发起信任登录
    def get_passport_connect_wap(self, type, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   type        登录类型,可用值:QQ,WEIBO,WECHAT,ALIPAY
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_wap')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 微信发起授权
    def get_passport_connect_wechat(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_wechat')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 微信发起授权回调
    def get_passport_connect_wechat_back(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_wechat_back')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 自动登录api
    def get_passport_connect_wechat_login(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   uuid         客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_wechat_login')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 信任登录统一回调地址
    def get_passport_connect_callback(self, port, type, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   type         登录类型,可用值:QQ,WEIBO,WECHAT,ALIPAY
                        port         登录客户端,可用值:PC,WAP
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_connect_callback')
        self.suffix = self.suffix.format(port, type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # pc登录绑定
    def put_passport_loginBinder_pc(self, uuid_connect, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username        用户名
                        password        密码
                        captcha         验证码
                        uuid            客户端唯一标识
                        uuid_connect    客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginBinder_pc')
        self.suffix = self.suffix.format(uuid_connect)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # WAP登录绑定
    def post_passport_loginBinder_wap(self, uuid, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username        用户名
                        password        密码
                        captcha         验证码
                        uuid            客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_loginBinder_wap')
        self.suffix = self.suffix.format(uuid)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # WAP发送手机验证码
    def post_passport_mobileBinder_smscode(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile          手机号
                        captcha         验证码
                        uuid            客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_mobileBinder_smscode')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # WAP手机绑定
    def post_passport_mobileBinder(self, uuid, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile          手机号
                        sms_code        手机验证码
                        uuid            客户端唯一标识
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_mobileBinder')
        self.suffix = self.suffix.format(uuid)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)

