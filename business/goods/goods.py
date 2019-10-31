#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: select_goods.py
    @time: 2019/10/31 14:18
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.recordlog import logs
from common.config import Config

class Goods(Requests_Test):

    def __init__(self):
        self.c = Config()
        self.prefix1 = self.c.get_value('URL', 'dev_url')
        self.prefix2 = self.c.get_value('URL', 'url')

    # 查询商品
    def dev_goods(self, goods_id):
        # 读取配置文件里的数据
        suffix = self.c.get_value('Goods', 'goods')

        # 拼成url
        url = self.prefix1 + suffix + str(goods_id)
        logs.info('测试接口为：%s' % url)
        return self.get_requests(url)

    def goods(self, goods_id):
        suffix = self.c.get_value('Goods', 'goods')

        # 拼成url
        url = self.prefix2 + suffix + str(goods_id)
        logs.info('测试接口为：%s' % url)
        return self.get_requests(url, prod=True)


if __name__ == '__main__':
    g = Goods()
    result = g.dev_goods(345)
    result2 = g.goods(345)
    print(result.text)
    print(result2.text)
