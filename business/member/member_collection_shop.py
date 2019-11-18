# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_collection_shop.py
    @time: 2019/11/13 16:53
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Collection_Shop(Requests_Test):

    # 添加会员收藏店铺
    def post_member_collection_shop(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   shop_id            店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_collection_shop')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 查看会员是否收藏店铺
    def get_member_collection_shop_id(self, shop_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   shop_id            要检索的收藏店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_collection_shop_id')
        self.suffix = self.suffix.format(shop_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 删除会员收藏店铺
    def del_member_collection_shop_id(self, shop_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   shop_id            要删除的店铺id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_collection_shop_id')
        self.suffix = self.suffix.format(shop_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询会员收藏店铺列表
    def get_member_collection_shops(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   page_no             页码
                        page_size           每页显示数量
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_collection_shops')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Collection_Shop()
    post_data = {'shop_id' : '19'}

    # result = m.post_member_collection_shop('13412345678', '123456', post_data)
    # result = m.get_member_collection_shop_id('19', '13412345678', '123456')
    # result = m.get_member_collection_shops('13412345678', '123456')
    result = m.del_member_collection_shop_id('19', '13412345678', '123456')
    print(result)
    print(result.text)