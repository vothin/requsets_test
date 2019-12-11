# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: change_requests.py
    @time: 2019/12/11 12:00
    @desc:
'''
# ********************************************************

import json, uuid, time, random
from common.change_md5 import get_md5
from common.recordlog import logs
from business.passport.passport_login_noCaptcha import Passport_LoginNo
from business.device.ncs_login import Ncs_Login

class Change_Requests():

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


    # 获得requests响应正文
    def get_json(self):
        response = ''

        logs.info('get login')

        # 获取response
        if self.prod == None or self.prod == 2 or self.prod == 3:
            p = Passport_LoginNo()
            response = p.get_passport_loginno(self.username, self.password, self.headers, self.prod)

        elif self.prod == 4 or self.prod == 5 or self.prod == 6:
            pass

        elif self.prod == 10 or self.prod == 11 or self.prod == 12:
            n = Ncs_Login()
            response = n.get_ncs_device_login(self.username, self.password, self.headers, self.prod)


        logs.info('login url:%s' % response.url)
        logs.info(response)

        # json格式阅读
        js = json.loads(response.text)

        return js

