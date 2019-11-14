# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: checkout_param.py
    @time: 2019/11/8 11:11
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Checkout_Param(Requests_Test):

    # 获取结算参数
    def get_checkout_params(self, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 设置收货地址id
    def post_checkout_params_addressId(self, address_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  address_id          收货地址id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params_addressId')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 设置支付类型
    def post_checkout_params_payType(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  payment_type          支付类型 在线支付：ONLINE，货到付款：COD,可用值:ONLINE,COD
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params_payType')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 设置发票信息
    def post_checkout_params_receipt(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  receipt_title           发票抬头
                        receipt_content         发票内容
                        tax_no                  发票税号
                        type                    普票类型，0为个人，其他为公司
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params_receipt')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)




    # 取消发票
    def del_checkout_params_receipt(self, username=None, password=None, data=None, prod=False):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params_receipt_del')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 设置送货时间
    def post_checkout_params_receiveTime(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  receive_time           送货时间
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params_receiveTime')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 设置订单备注
    def post_checkout_params_remark(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  receive_time           送货时间
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Deal', 'checkout_params_remark')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


if __name__ == '__main__':
    c = Checkout_Param()

    result = c.get_checkout_params('15652179020', 'qqqqqq')
    print(result)
    print(result.text)


