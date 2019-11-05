# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_categories.py
    @time: 2019/10/31 18:23
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.recordlog import logs
from common.change_urls import Change_Urls

class Goods_Categories(Requests_Test):

    # 首页等商品分类数据
    def url_goods_categories(self, parent_id, username=None, password=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_categories')
        self.suffix = self.suffix.format(parent_id)

        cu = Change_Urls()
        # gu = cu.get_urls(suffix=self.suffix, username=username, password=password, prod=prod)
        gu = cu.get_urls(self.suffix, username, password, prod=prod)

        return self.get_requests(gu[0], gu[1])


if __name__ == '__main__':
    g = Goods_Categories()
    result = g.url_goods_categories(2, '13412345678', '123456', prod=True)
    print(result.text)