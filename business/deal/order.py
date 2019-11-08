# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: order.py
    @time: 2019/11/7 16:44
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Order(Requests_Test):


    def get_tarde_order_listo2o(self, username=None, password=None, data=None, prod=False):

        '''
            相关参数有：  goods_name          	商品名称关键字
                        key_words           关键字
                        order_status        订单状态,可用值:ALL,WAIT_PAY,WAIT_SHIP,WAIT_ROG,CANCELLED,COMPLETE,WAIT_COMMENT,REFUND
                        page_no             页数
                        page_size           条数
        '''
        self.suffix = self.c.get_value('Deal', 'trade_orders_listo2o')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



if __name__ == '__main__':
    o = Order()
    result = o.get_tarde_order_listo2o()
    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)
