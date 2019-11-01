# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: get_headers.py
    @time: 2019/11/1 11:27
    @desc:
'''
# ********************************************************


import json, uuid, time, random
from common.get_md5 import change_md5
from common.recordlog import logs
from business.passport.passport_login_noCaptcha import Passport_LoginNo

class Get_Headers():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.uuid = uuid.uuid4()
        self.timestamp = str(time.time() * 1000)
        self.nonce = str(random.randint(100000, 999999))
        self.sign = ''

    # 获得requests响应正文
    def get_json(self):

        logs.info('get response to json')
        p = Passport_LoginNo()
        response = p.url_passport_loginno(self.username, self.password)
        js = json.loads(response.text)

        return js


    # 输入请求头headers
    def set_headers(self):
        logs.info('set headers')

        js = self.get_json()
        logs.info('response:%s' % js)
        print(js['access_token'])           #  !!!!


        try:
            js['access_token']
        except Exception as e:
            logs.error('login failure', e)
        else:
            sign = str(js['uid']) + self.nonce + self.timestamp + str(js['access_token'])
            self.sign = change_md5(sign)

            headers = {
                'Authorization' : js['access_token'],
                'uuid' : self.uuid
            }

            url = '?uid='+ str(js['uid']) \
                  + "&timestamp=" + self.timestamp \
                  + "&nonce=" + self.nonce \
                  + "&sign" + sign
            return headers, url


if __name__ == '__main__':
    g = Get_Headers('13412345678', '123456')
    result = g.set_headers()
    print(result)
