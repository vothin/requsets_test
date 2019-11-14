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
from common.change_urltail import Change_UrlTail
from common.requests_test import Requests_Test

class Change_Param():

    def __init__(self, username=None, password=None, prod=False):
        self.username = username
        self.password = password
        self.headers  = None
        self.url_tail = ''
        self.prod = prod


    def get_params(self):

        # 判断是否登录
        if self.username:
            ch = Change_UrlTail(self.username, self.password, self.prod)
            gh = ch.get_urlTail()
            self.headers = gh[0]
            self.url_tail = gh[1]

            return self.headers, self.url_tail

        else:
            logs.info('Not Parameter')
            return self.headers, self.url_tail


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

    prod = True

    cu = Change_Param('13412345678', '123456')
    gu = cu.get_params()

    # print(gu)




