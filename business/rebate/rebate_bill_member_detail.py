# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: rebate_bill_member_detail.py
    @time: 2019/12/24 11:15
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs

class Rebate_Bill_Member_Detail(Requests_Test):

    # 分润统计图表
    def get_rebate_bill_member_detail_chartdata(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_bill_member_detail_chartdata')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 分润统计图表
    def get_rebate_bill_member_detail_chartdataNoMemberId(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_bill_member_detail_chartdataNoMemberId')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询列表
    def post_rebate_bill_member_detail_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_bill_member_detail_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询最近三天列表
    def post_rebate_bill_member_detail_recent_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_bill_member_detail_recent_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



if __name__ == '__main__':
    r = Rebate_Bill_Member_Detail()

    get_data = {
        'member_id' : '4473'
    }

    post_data = {
        'page_no': '1',
        'page_size': '10'
    }

    # result = r.get_rebate_bill_member_detail_chartdata('16312345678', '123456', get_data, prod=4)
    # result = r.get_rebate_bill_member_detail_chartdataNoMemberId('16312345678', '123456', prod=4)
    # result = r.post_rebate_bill_member_detail_page('16312345678', '123456', post_data, prod=4)
    result = r.post_rebate_bill_member_detail_recent_page('16312345678', '123456', prod=4)

    print(result)
    print(result.text)