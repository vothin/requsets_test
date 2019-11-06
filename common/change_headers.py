# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: change_headers.py
    @time: 2019/11/1 11:27
    @desc:
'''
# ********************************************************


import json, uuid, time, random
from common.change_md5 import get_md5
from common.recordlog import logs
from business.passport.passport_login_noCaptcha import Passport_LoginNo

class Change_Headers():

    def __init__(self, username, password, prod=False):
        self.username = username                            # 登录账号
        self.password = password                            # 登录密码
        self.uuid = str(uuid.uuid4())                       # uuid参数
        self.timestamp = str(int(time.time()))       # timestamp参数

        self.nonce = str(random.randint(100000, 999999))    # nonce参数
        self.sign = ''                                      # sign参数
        self.prod = prod

    # 获得requests响应正文
    def get_json(self):
        logs.info('get response to json')

        # 获取response
        p = Passport_LoginNo()
        response = p.get_passport_loginno(self.username, self.password, self.prod)

        # json格式阅读
        js = json.loads(response.text)

        return js


    # 输入请求头headers
    def get_headers(self):
        logs.info('set headers')

        # 获得response的json格式
        js = self.get_json()
        logs.info('response:%s' % js)

        # 存在token就是登录成功
        if 'access_token' in js:
            sign = str(js['uid']) + self.nonce + self.timestamp + str(js['access_token'])
            self.sign = get_md5(sign)

            headers = {
                'Authorization' : js['access_token'],
                'uuid' : self.uuid
            }


            url_tail = {
                'uid'       : str(js['uid']),
                'timestamp' : self.timestamp,
                'nonce'     : self.nonce,
                'sign'      : self.sign
            }

            return headers, url_tail

        else:
            logs.error('not found access_token')

if __name__ == '__main__':
    g = Change_Headers('13412345678', '123456')
    result = g.get_headers()
    print(result)
