# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_login_noCaptcha.py
    @time: 2019/11/1 10:42
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.recordlog import logs
from common.change_md5 import get_md5

class Passport_LoginNo(Requests_Test):

    # 查询商品列表
    def url_passport_loginno(self, username, password, prod=False):
        self.suffix = self.c.get_value('passport', 'passport_login_noCaptcha')

        password = get_md5(password)

        self.url = self.url_joint(prod) + '?username=' + username + '&password=' + password

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url)

if __name__ == '__main__':
    p = Passport_LoginNo()
    result = p.url_passport_loginno('13412345678', '123456')
    print(result.text)