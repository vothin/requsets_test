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

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 根据交易编号或者订单编号查询收银台数据
    def get_tarde_order_cashier(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  trade_sn            交易编号
                        order_sn            订单编号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_cashier')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


    # 查询O2O会员订单列表
    def get_tarde_order_listo2o(self, username=None, password=None, data=None, prod=False):

        '''
            相关参数有：  goods_name          	商品名称关键字
                        key_words           关键字
                        order_status        订单状态,可用值:ALL,WAIT_PAY,WAIT_SHIP,WAIT_ROG,CANCELLED,COMPLETE,WAIT_COMMENT,REFUND
                        page_no             页数
                        page_size           条数
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_listo2o')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)




    # 查询订单状态的数量
    def get_tarde_order_statusNum(self, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_statusNum')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询单个订单明细
    def get_tarde_order_sn(self, order_sn,  username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_sn')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 取消订单
    def post_tarde_order_cancel(self, order_sn,  username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_cancel')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 订单流程图数据
    def get_tarde_order_flow(self, order_sn,  username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_flow')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询订单日志
    def get_tarde_order_log(self, order_sn,  username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_log')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 确认收货
    def post_tarde_order_rog(self, order_sn,  username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_rog')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 根据交易编号查询订单列表
    def get_tarde_order_list(self, trade_sn,  username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'trade_orders_list')
        self.suffix = self.suffix.format(trade_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)






if __name__ == '__main__':
    o = Order()

    data = {
        'page_no' : '1',
        'page_size' : '1'
    }

    trade_sn = {'trade_sn' : '20190924000002'}

    order_sn = {'order_sn' : '20190924000002'}

    reason = {'reason' : '???'}

    # result = o.get_tarde_order('13412345678', '123456', data)
    # result = o.get_tarde_order_cashier('13412345678', '123456', trade_sn)
    # result = o.get_tarde_order_cashier('13412345678', '123456', order_sn)
    # result = o.get_tarde_order_listo2o('13412345678', '123456', data)
    # result = o.get_tarde_order_statusNum('13412345678', '123456')
    # result = o.get_tarde_order_sn('20190924000002', '13412345678', '123456')
    # result = o.post_tarde_order_cancel('20190924000002', '13412345678', '123456', reason)
    # result = o.get_tarde_order_flow('20190924000002', '13412345678', '123456')
    # result = o.get_tarde_order_log(order_sn['order_sn'], '13412345678', '123456')
    # result = o.post_tarde_order_rog(order_sn['order_sn'], '13412345678', '123456')
    result = o.get_tarde_order_list(trade_sn['trade_sn'], '13412345678', '123456')
    print(result)
    print(result.text)
