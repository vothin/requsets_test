# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: change_urls.py
    @time: 2019/11/5 11:29
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_headers import Change_Headers
from common.change_data import Change_Data

class Change_Param():

    def __init__(self, username=None, password=None, data=None):
        self.username = username
        self.password = password
        self.data     = data
        self.headers  = None

    def get_params(self):
        # 判断是否需要token
        if self.username:
            if self.data:
                ch = Change_Headers(self.username, self.password)
                gh = ch.get_headers()
                self.headers = gh[0]

                ck = Change_Data(self.data, gh[1])
                self.data = ck.get_data()

                logs.info('Test data:%s' % self.data)
                return self.headers, self.data

            else:
                ch = Change_Headers(self.username, self.password)
                gh = ch.get_headers()
                self.headers = gh[0]

                self.data = gh[1]

                return self.headers, self.data

        else:
            if self.data:
                logs.info('Test data:%s' % self.data)
                return self.headers, self.data

            else:
                logs.info('Not Parameter')
                return self.headers, self.data







        # if data:
        #     ck = Change_Kwargs(data)
        #     gk = ck.get_kwargs()
        #
        #     # 判断是否需要token
        #     if username != None:
        #         ch = Change_Headers(username, password, prod)
        #         gh = ch.get_headers()
        #         self.headers = gh[0]
        #
        #         self.url = self.url_joint(prod) + '?' + gk + gh[1]
        #     else:
        #         self.url = self.url_joint(prod) + '?' + gk[:-1]
        #
        # else:
        #     # 判断是否需要token
        #     if username != None:
        #         ch = Change_Headers(username, password, prod)
        #         gh = ch.get_headers()
        #         self.headers = gh[0]
        #
        #         self.url = self.url_joint(prod) + '?' + gh[1]
        #     else:
        #         self.url = self.url_joint(prod)
        #
        # logs.info('Test interface:%s' % self.url)
        # return self.url, self.headers


if __name__ == '__main__':
    pass

