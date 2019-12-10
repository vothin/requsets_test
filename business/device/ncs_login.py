# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: ncs_login.py
    @time: 2019/12/10 15:56
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_md5 import get_md5

class Ncs_Login(Requests_Test):

    # 无验证登录
    def get_ncs_device_login(self, username, password, captcha, headers, prod=None):
        self.suffix = self.c.get_value('Device', 'ncs_device_login')
        self.url = self.url_joint(prod)

        password = get_md5(str(password))

        data = {
            'username' : str(username),
            'password' : str(password),
            'captcha'  : str(captcha),
            'uuid'     : '777'
        }

        return self.get_requests(self.url, headers, data)


if __name__ == '__main__':
    n = Ncs_Login()
    headers = {
        'uuid' : '777'
    }
    result = n.get_ncs_device_login('16312345678', '123456', 'fct8', headers, prod=8)
    print(result)
    print(result.text)
    print(result.url)