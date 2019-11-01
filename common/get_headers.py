# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: get_headers.py
    @time: 2019/11/1 11:27
    @desc:
'''
# ********************************************************


import json
from business.passport.passport_login_noCaptcha import Passport_LoginNo

class Get_Headers():

    def __init__(self, username, password):
        self.username = username
        self.password = password


    # 获得requests响应正文
    def get_json(self):

        p = Passport_LoginNo()
        response = p.url_passport_loginno(self.username, self.password)
        js = json.loads(response.text)
        return js


    # 输入请求头headers
    def set_headers(self):
        js = self.get_json()
        headers = {
            'Authorization': js['access_token'],
            'uid': js['uid']
        }


if __name__ == '__main__':
    pass