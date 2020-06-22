# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: rebate_detail_member.py
    @time: 2019/12/24 11:35
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Rebate_Detail_Member(Requests_Test):

    # 查询列表
    def post_rebate_detail_member_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_detail_member_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)


if __name__ == '__main__':
    r = Rebate_Detail_Member()

    post_data = {
        'member_id' : '4473',
        'page_no': '1',
        'page_size': '10'
    }

    result = r.post_rebate_detail_member_page('16312345678', '123456', post_data, prod=4)

    print(result)
    print(result.text)