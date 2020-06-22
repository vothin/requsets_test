# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: passport_login_seller_noCaptcha.py
    @time: 2019/12/24 10:18
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_md5 import get_md5

class Passport_Login_Seller_NoCaptcha(Requests_Test):

    # 无验证登录
    def get_passport_login_seller_noCaptcha(self, username, password, headers, prod=None):
        self.suffix = self.c.get_value('Passport', 'passport_login_seller_noCaptcha')
        self.url = self.url_joint(prod)

        password = get_md5(str(password))

        data = {
            'username' : str(username),
            'password' : str(password)
        }

        return self.get_requests(self.url, headers, data)


if __name__ == '__main__':
    p = Passport_Login_Seller_NoCaptcha()

    headers = {
        'uuid' : '777'
    }

    result = p.get_passport_login_seller_noCaptcha('16312345678', '123456', headers, 4)
    print(result)
    print(result.text)