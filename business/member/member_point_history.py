# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_point_history.py
    @time: 2019/11/19 17:03
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Point_History(Requests_Test):

    # 查询会员积分列表
    def get_member_points(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   page_no             页码
                        page_size           每页显示数量
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_points')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询当前会员的积分
    def get_member_points_current(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_points_current')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Point_History()
    # result = m.get_member_points('13412345678', '123456')
    result = m.get_member_points_current('13412345678', '123456')
    print(result)
    print(result.text)