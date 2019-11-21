# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: promotions.py
    @time: 2019/11/21 16:38
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Promotions(Requests_Test):


    # 根据商品读取参与的所有活动
    def get_promotions_goodsId(self, goods_id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_goodsId')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    p = Promotions()

    result = p.get_promotions_goodsId('343')
    print(result)
    print(result.text)