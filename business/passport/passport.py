# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport.py
    @time: 2019/11/20 11:50
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Passport(Requests_Test):


    # 手机号重复校验
    def get_passport_mobile(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile        手机号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_mobile')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 验证手机验证码
    def get_passport_smscode(self, mobile, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   mobile          手机号
                        sms_code        验证码
                        scene           业务类型
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_smscode')
        self.suffix = self.suffix.format(mobile)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 刷新token
    def post_passpost_token(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   refresh_token      刷新token
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_token')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 用户名重复校验
    def get_passport_username(self, uname, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   username        用户名
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Passport', 'passport_username')
        self.suffix = self.suffix.format(uname)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    p = Passport()

    # result = p.get_passport_mobile('13412345678', '13412345678', '123456')
    result = p.get_passport_username('tsuser01', '13412345678', '123456')

    print(result)
    print(result.text)