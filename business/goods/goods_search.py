# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_search.py
    @time: 2019/11/1 9:55
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.recordlog import logs

class Goods_Search(Requests_Test):

    # 查询商品列表
    def url_goods_search(self, page_no=None, page_size=None, keyword=None, category=None, brand=None, price=None, sort=None, prop=None, seller_id=None, shop_cat_id=None, prod=False):
        self.suffix = self.c.get_value('Goods', 'goods_categories')

        self.url = self.url_joint(prod)

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url)


if __name__ == '__main__':
    g = Goods_Search()
    result = g.url_goods_search()
    print(result)