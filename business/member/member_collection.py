# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_collection.py
    @time: 2019/11/13 15:07
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Collection(Requests_Test):

    # 查询会员商品收藏列表
    def get_member_collection_goods(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   page_no             页码
                        page_size           每页显示数量
        '''
        self.suffix = self.c.get_value('Member', 'members_collection_goods')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 添加会员商品收藏
    def post_member_collection_goods(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   goods_id            商品id
        '''
        self.suffix = self.c.get_value('Member', 'members_collection_goods')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 删除会员商品收藏
    def del_member_collection_goods(self, goods_id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   goods_id            商品id
        '''
        self.suffix = self.c.get_value('Member', 'members_collection_goods_del')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0], gu[1])



    # 查询会员是否收藏商品
    def get_member_collection_goods_id(self, id, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   id            商品id
        '''
        self.suffix = self.c.get_value('Member', 'members_collection_goods_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])







