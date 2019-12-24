# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: rebate_bill_member.py
    @time: 2019/12/24 10:06
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Rebate_Bill_Member(Requests_Test):

    # 分润统计图表
    def get_rebate_bill_member_chartdata(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_bill_member_chartdata')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    r = Rebate_Bill_Member()

    get_data = {
        'member_id' : '4473'
    }

    result = r.get_rebate_bill_member_chartdata('16312345678', '123456', data=get_data, prod=4)