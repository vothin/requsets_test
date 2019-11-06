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

    # 无验证登录
    def get_passport_loginno(self, username, password, prod=False):
        self.suffix = self.c.get_value('Passport', 'passport_login_noCaptcha')
        self.url = self.url_joint(prod)

        password = get_md5(str(password))

        up = {
            'username' : str(username),
            'password' : str(password)
        }

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, get_data=up)

if __name__ == '__main__':
    p = Passport_LoginNo()
    result = p.get_passport_loginno('13412345678', '123456', prod=True)
    print(result)
    print(result.text)