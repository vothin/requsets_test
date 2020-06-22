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
from common.change_param import Change_Param

class Goods_Categories(Requests_Test):

    # 首页等商品分类数据
    def get_goods_categories(self, parent_id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Goods', 'goods_categories')
        self.suffix = self.suffix.format(parent_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


if __name__ == '__main__':
    g = Goods_Categories()
    result = g.get_goods_categories(2, '13412345678', '123456', prod=True)
    print(result.text)