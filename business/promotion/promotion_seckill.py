# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: promotion_seckill.py
    @time: 2019/11/21 16:41
    @desc:
'''
# ********************************************************



from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Promotion_Seckill(Requests_Test):

    # 根据参数读取限时抢购的商品列表
    def get_promotions_seckill_goodslist(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_seckill_goodslist')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 读取秒杀时刻
    def get_promotions_seckill_timeline(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Promotion', 'promotions_seckill_timeline')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    p = Promotion_Seckill()

    get_data = {'range_time' : '1'}

    # result = p.get_promotions_seckill_goodslist(data=get_data)
    result = p.get_promotions_seckill_timeline()
    print(result)
    print(result.text)