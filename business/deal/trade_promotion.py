# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: trade_promotion.py
    @time: 2019/11/11 14:46
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Trade_promotion(Requests_Test):

    # 选择要参与的促销活动
    def post_tarde_create(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  seller_id           卖家id
                        sku_id              产品id
                        activity_id         活动id
                        promotion_type      活动类型
        '''
        self.suffix = self.c.get_value('Deal', 'trade_promotion')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 取消参与促销
    def del_tarde_create(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  seller_id           卖家id
                        sku_id              产品id
                        sellerId            sellerId
                        skuId               skuId
        '''
        self.suffix = self.c.get_value('Deal', 'trade_promotion_del')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0], gu[1])



    # 设置O2O优惠券
    def post_tarde_o2o_coupon(self, seller_id, mc_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  seller_id           卖家ID
                        mc_id               优惠券ID
            使用优惠券的时候分为三种情况：
                前2种情况couponId 不为0,不为空。
                第3种情况couponId为0,
                    1、使用优惠券:在刚进入订单结算页，为使用任何优惠券之前。
                    2、切换优惠券:在1、情况之后，当用户切换优惠券的时候。
                    3、取消已使用的优惠券:用户不想使用优惠券的时候。
        '''
        self.suffix = self.c.get_value('Deal', 'trade_promotion_o2o_coupon')
        self.suffix = self.suffix.format(seller_id, mc_id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 设置优惠券
    def post_tarde_coupon(self, seller_id, mc_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  seller_id           卖家ID
                        mc_id               优惠券ID
            使用优惠券的时候分为三种情况：
                前2种情况couponId 不为0,不为空。
                第3种情况couponId为0,
                    1、使用优惠券:在刚进入订单结算页，为使用任何优惠券之前。
                    2、切换优惠券:在1、情况之后，当用户切换优惠券的时候。
                    3、取消已使用的优惠券:用户不想使用优惠券的时候。
        '''
        self.suffix = self.c.get_value('Deal', 'trade_promotion_coupon')
        self.suffix = self.suffix.format(seller_id, mc_id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



