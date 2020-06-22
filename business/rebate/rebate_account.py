# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: rebate_account.py
    @time: 2019/12/24 17:15
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Rebate_Account(Requests_Test):

    # 添加分润提现银行卡
    def post_rebate_account(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询分润提现银行卡列表
    def post_rebate_account_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 删除分润提现银行卡
    def del_rebate_account_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个分润提现银行卡复制
    def get_rebate_account_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改分润提现银行卡
    def put_rebate_account_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)


if __name__ == '__main__':
    r = Rebate_Account()

    post_data = {
        'memberId' : '4473',
        'bankName' : 'yinhang1',
        'bankAccount' : '1231',
        'accountName' : 'yinhangyonghuming'
    }

    post_data1 = {
        'page_no': '1',
        'page_size': '10'
    }

    put_data = {
        'memberId' : '4473',
        'bankName' : 'yinhang2',
        'bankAccount' : '456',
        'accountName' : '456'
    }

    # result = r.post_rebate_account('16312345678', '123456', post_data, prod=4)
    # result = r.post_rebate_account_page('16312345678', '123456', post_data1, prod=4)
    # result = r.del_rebate_account_ids('0', '16312345678', '123456', prod=4)
    # result = r.get_rebate_account_ids('0', '16312345678', '123456', prod=4)
    result = r.put_rebate_account_ids('0', '16312345678', '123456', put_data, prod=4)
    print(result)
    print(result.text)
    print(result.url)