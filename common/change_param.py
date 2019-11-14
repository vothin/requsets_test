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

class Change_Param():

    def __init__(self, username=None, password=None, data=None):
        self.username = username
        self.password = password
        self.data     = data
        self.headers  = None
        self.url_tail = None


    def get_params(self):
        # 判断是否需要登录
        if self.username:

            # 判断是否存在data
            if self.data:           # 存在headers和data
                ch = Change_Headers(self.username, self.password)
                gh = ch.get_headers()
                self.headers = gh[0]
                self.url_tail = gh[1]

                logs.info('data:%s' % self.data)
                return self.headers, self.data, self.url_tail

            else:                   # 只存在headers
                ch = Change_Headers(self.username, self.password)
                gh = ch.get_headers()
                self.headers = gh[0]
                self.url_tail = gh[1]


                logs.info('data:%s' % self.data)
                return self.headers, self.data, self.url_tail

        else:                       # 只存在data
            if self.data:
                logs.info('Test data:%s' % self.data)
                return self.headers, self.data, self.url_tail

            else:                   # 什么都不存在
                logs.info('Not Parameter')
                return self.headers, self.data, self.url_tail




if __name__ == '__main__':
    from common.config import Config
    from base.base import Base
    from common.requests_test import Requests_Test
    c = Config()
    Base.suffix = c.get_value('Goods', 'goods_categories')
    Base.suffix = Base.suffix.format(2)

    data = {
        'test' : 'test'
    }

    cu = Change_Param('13412345678', '123456', data)
    gu = cu.get_params()
    print(gu)




