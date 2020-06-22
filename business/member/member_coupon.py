# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_coupon.py
    @time: 2019/11/19 10:30
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Coupon(Requests_Test):

    # 查询我的优惠券列表
    def get_member_coupon(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   status              优惠券状态 0为全部，1为未使用且可用，2为已使用，3为已过期, 4为不可用优惠券（已使用和已过期）,可用值:0,1,2,3,4
                        page_no             页数
                        page_size           条数
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_coupon')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 优惠券—未使用,已使用,已过期状态总数量
    def get_member_coupon_num(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_coupon_num')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 用户领取优惠卷
    def post_member_coupon_receive(self, coupon_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   coupon_id          优惠券id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_coupon_receive')
        self.suffix = self.suffix.format(coupon_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 结算页—读取可用的优惠券列表
    def get_member_coupon_sellerIds(self, seller_ids, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   seller_ids          商家ID集合
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_coupon_sellerIds')
        self.suffix = self.suffix.format(seller_ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Coupon()
    # result = m.get_member_coupon('13412345678', '123456')
    # result = m.get_member_coupon_num('13412345678', '123456')
    # result = m.post_member_coupon_receive('22', '13412345678', '123456')
    result = m.get_member_coupon_sellerIds('20', '13412345678', '123456')

    print(result)
    print(result.text)


