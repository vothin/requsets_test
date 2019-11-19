# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_connect.py
    @time: 2019/11/19 10:10
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Connent(Requests_Test):

    # 获取绑定列表API
    def get_member_AB_list(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_connect_AB_list')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 登录绑定openid
    def post_member_AB_login(self, uuid, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_connect_AB_login')
        self.suffix = self.suffix.format(uuid)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 发起账号绑定
    def get_member_AB_pc(self, type, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_connect_AB_pc')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 注册绑定openid
    def post_member_AB_register(self, uuid, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_connect_AB_register')
        self.suffix = self.suffix.format(uuid)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 微信退出解绑操作
    def post_member_AB_unbindOUT(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_connect_AB_unbindOUT')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 会员解绑操作
    def post_member_AB_unbind(self, type, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_connect_AB_unbind')
        self.suffix = self.suffix.format(type)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Connent()
    # reslut = m.get_member_AB_list('13412345678', '123456')
    reslut = m.post_member_AB_login('777', '13412345678', '123456')


    print(reslut)
    print(reslut.text)