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

    # 查询会员订单列表
    def get_tarde_order(self, username=None, password=None, data=None, prod=False):

        '''
            相关参数有：  goods_name          	商品名称关键字
                        key_words           关键字
                        order_status        订单状态,可用值:ALL,WAIT_PAY,WAIT_SHIP,WAIT_ROG,CANCELLED,COMPLETE,WAIT_COMMENT,REFUND
                        page_no             页数
                        page_size           条数
        '''
        self.suffix = self.c.get_value('Deal', 'trade_orders')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 根据交易编号或者订单编号查询收银台数据
    def get_tarde_order_cashier(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  trade_sn            交易编号
                        order_sn            订单编号
        '''
        self.suffix = self.c.get_value('Deal', 'trade_orders_cashier')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 查询O2O会员订单列表
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



    # 查询订单状态的数量
    def get_tarde_order_statusNum(self, username=None, password=None, data=None, prod=False):

        self.suffix = self.c.get_value('Deal', 'trade_orders_statusNum')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 查询单个订单明细
    def get_tarde_order_sn(self, order_sn,  username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'trade_orders_sn')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 取消订单
    def post_tarde_order_cancel(self, order_sn,  username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'tarde_orders_cancel')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 订单流程图数据
    def get_tarde_order_flow(self, order_sn,  username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'tarde_orders_flow')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 查询订单日志
    def get_tarde_order_log(self, order_sn,  username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'tarde_orders_log')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 确认收货
    def post_tarde_order_rog(self, order_sn,  username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'tarde_orders_rog')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 根据交易编号查询订单列表
    def get_tarde_order_list(self, trade_sn,  username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'tarde_orders_list')
        self.suffix = self.suffix.format(trade_sn)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])





if __name__ == '__main__':
    o = Order()
    # result = o.get_tarde_order_listo2o()
    result = o.get_tarde_order_statusNum('13412345678', '123456')
    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)
