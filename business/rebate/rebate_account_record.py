# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: rebate_account_record.py
    @time: 2019/12/24 17:31
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Rebate_Account_Record(Requests_Test):

    # 添加分润银行卡提现记录
    def post_rebate_account_record(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_record')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询分润银行卡提现记录列表
    def post_rebate_account_record_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_record_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询一个分润银行卡提现记录
    def get_rebate_account_record_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Rebate', 'rebate_account_record_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Rebate_Account_Record()

    post_data = {
        'rebate_account_id' : '1',
        'memberId' : '4473',
        'bankName' : 'yinhang1',
        'bankAccount' : '1231',
        'accountName' : 'yinhangyonghuming',
        'amount' : '1',
        'type' : '1'
    }


    post_data1 = {
        'page_no': '1',
        'page_size': '10'
    }

    # result = c.post_rebate_account_record('16312345678', '123456', post_data, prod=4)
    # result = c.post_rebate_account_record_page('16312345678', '123456', post_data1, prod=4)
    result = c.get_rebate_account_record_ids('1', '16312345678', '123456', prod=4)

    print(result)
    print(result.text)
