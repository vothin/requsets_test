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

                logs.info('Test data:%s' % self.data)
                return self.headers, self.data

        else:
            if self.data:
                logs.info('Test data:%s' % self.data)
                return self.headers, self.data

            else:
                logs.info('Not Parameter')
                return self.headers, self.data



    def get_params_alt(self):

        if self.username:
            ch = Change_Headers(self.username, self.password)
            gh = ch.get_headers_alt()
            self.headers = gh[0]

            if self.data:
                ck = Change_Data(self.data)
                self.data = ck.get_data_alt()

                self.data = self.data + gh[1]

                return self.headers, self.data

            else:
                self.data = gh[1]
                return self.headers, self.data

        else:
            if self.data:
                ck = Change_Data(self.data)
                self.data = ck.get_data_alt()[:-1]

                return self.headers, self.data

            else:
                return self.headers, self.data


if __name__ == '__main__':
    from common.config import Config
    from base.base import Base
    from common.requests_test import Requests_Test
    c = Config()
    Base.suffix = c.get_value('Goods', 'goods_categories')
    Base.suffix = Base.suffix.format(2)

    cu = Change_Param()
    gu = cu.get_params()
    print(gu)

    result = cu.get_params()
    print(result)



