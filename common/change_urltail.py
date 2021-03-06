# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: change_urltail.py
    @time: 2019/11/1 11:27
    @desc:
'''
# ********************************************************


import time, random
from common.change_md5 import get_md5
from common.recordlog import logs
from common.change_requests import Change_Requests

class Change_UrlTail():

    def __init__(self, username, password, prod=None):
        self.username = username                            # 登录账号
        self.password = password                            # 登录密码
        self.uuid = '777'                                   # uuid参数
        self.timestamp = str(int(time.time()) * 1000)       # timestamp参数

        self.nonce = str(random.randint(100000, 999999))    # nonce参数
        self.sign = ''                                      # sign参数
        self.prod = prod
        self.headers = {'uuid' : self.uuid}
        self.url_tail = ''


    # 输入请求头headers
    def get_urlTail(self):
        logs.info('get headers')

        # 获得response的json格式
        c = Change_Requests(self.username, self.password, self.prod)
        js = c.get_json()

        # 存在token就是登录成功
        if 'access_token' in js:
            sign = str(js['uid']) + self.nonce + self.timestamp + str(js['access_token'])
            self.sign = get_md5(sign)

            # 生成url拼接部分
            self.url_tail = '?uid=' + str(js['uid']) + '&timestamp=' + self.timestamp + '&nonce=' + self.nonce + '&sign=' + self.sign

            return self.headers, self.url_tail

        else:
            logs.error('not found access_token')
            return self.headers, self.url_tail



if __name__ == '__main__':

    # headers = {'uuid' : '777'}
    captcha = '3tqk'

    g = Change_UrlTail('16312345678', '123456', 10)


    # result = g.get_urlTail()

    # result = g.get_device_cap_urlTail()
    result = g.get_json()

    print(result)
