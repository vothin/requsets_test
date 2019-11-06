# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_taps.py
    @time: 2019/11/5 15:22
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Goods_Taps(Requests_Test):        # 未完成

    # 查询商品销量
    def get_goods_count(self, goods_id, username=None, password=None, prod=False):

        self.suffix = self.c.get_value('Goods', 'goods_tags_count')

        self.url = self.url_joint(prod)
        logs.info('Test interface:%s' % self.url)

        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        return self.get_requests(self.url, gu[0], gu[1])



if __name__ == '__main__':
    g = Goods_Taps()
    data = {
        'goods_id' : 16
    }

    resutl = g.get_goods_count(data, '13412345678', '123456')
    print(resutl)
    print(resutl.text)