# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_address.py
    @time: 2019/11/11 15:36
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Address(Requests_Test):

    # 添加会员地址
    def post_member_address(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   name                        收货人姓名
                        addr                        详细地址
                        tel                         联系电话(一般指座机)
                        mobile                      手机号码
                        def_addr                    是否为默认收货地址,1为默认
                        ship_address_name           地址别名
                        region                      地区
        '''
        self.suffix = self.c.get_value('Member', 'members_address')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 查询当前会员的某个地址
    def get_member_address_id(self, id,  username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  id          要查询的地址id
        '''
        self.suffix = self.c.get_value('Member', 'members_address_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 修改会员地址
    def put_member_address_id(self, id,  username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   id                      主键
                        name                    收货人姓名
                        addr                    详细地址
                        tel                     联系电话(一般指座机)
                        mobile                  手机号码
                        def_addr                是否为默认收货地址,1为默认
                        ship_address_name       地址别名
                        region                  地区
        '''
        self.suffix = self.c.get_value('Member', 'members_address_id_put')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.put_requests(self.url, gu[0], gu[1])



    # 删除会员地址
    def del_member_address_id(self, id,  username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   id                      要删除的会员地址id
        '''
        self.suffix = self.c.get_value('Member', 'members_address_id_del')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0], gu[1])



    # 设置地址为默认
    def put_member_address_id_default(self, id,  username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   id                      主键
        '''
        self.suffix = self.c.get_value('Member', 'members_address_id_default_put')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.put_requests(self.url, gu[0], gu[1])



    # 查询当前会员地址列表
    def get_member_addresses(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_addresses')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



