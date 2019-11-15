# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_sales.py
    @time: 2019/11/11 10:09
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Goods_Sales(Requests_Test):

    # 查询某商品的销售记录
    def get_goods_sales(self, goods_id, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'goods_sales')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    g = Goods_Sales()
    data = {
        'page_no' : '1',
        'page_size' : '1'
    }

    result = g.get_goods_sales(470, '13412345678', '123456', data)
    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)