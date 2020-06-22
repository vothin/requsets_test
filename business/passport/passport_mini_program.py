# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_mini_program.py
    @time: 2019/11/20 18:09
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Passport_Mini_Program(Requests_Test):


    # 小程序自动登录
    def get_passport_miniProgram_autoLogin(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   code                code
                        uuid                uuid
                        miniProgramType     miniProgramType
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_miniProgram_autoLogin')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 小程序绑定已有用户
    def post_passport_miniProgram_bindUser(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mini_program_type           小程序类型（miniprogramo2oseller,miniprogramo2obuyer）
                        code                        小程序登陆获取的code
                        uuid                        客户端唯一标识
                        username                    用户名
                        password                    密码
                        miniProgramType             miniProgramType
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_miniProgram_bindUser')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 获取微信小程序码
    def get_passport_miniProgram_codeUnlimit(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   miniProgramType     miniProgramType
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_miniProgram_codeUnlimit')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 加密数据解密验证
    def get_passport_miniProgram_decrypt(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   code                code
                        encryptedData       encryptedData
                        uuid                uuid
                        iv                  iv
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_miniProgram_decrypt')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 小程序注册绑定
    def post_passport_miniProgram_registerBind(self, uuid, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   nick_name           昵称
                        face                头像
                        uuid                客户端唯一标识
                        sex                 性别
                        mobile              手机号码
                        password            密码
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_miniProgram_registerBind')
        self.suffix = self.suffix.format(uuid)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)