# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_nurse_config.py
    @time: 2020/1/3 17:31
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Care_Nurse_Config(Requests_Test):

    # 添加护理配置
    def post_care_nurse_config(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_nurse_config')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询护理配置列表
    def post_care_nurse_config_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_nurse_config_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 删除护理配置
    def del_care_nurse_config_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_nurse_config_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个护理配置
    def get_care_nurse_config_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_nurse_config_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改护理配置
    def put_care_nurse_config_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_nurse_config_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)

if __name__ == '__main__':
    c = Care_Nurse_Config()

    post_data = {
        'part_id' : '3',
        'create_time' : '1578044822',
        'update_time' : '1578044822',
        'sync_time' : '1578044822',
        'nurse_level' : '4',
        'value' : '4',
        'his_value' : '1',
        'name' : 'name',
        'color': 'red',
        'content' : 'beizhu'
    }

    page = {
        'page_no' : '1',
        'page_size' : '10'
    }

    # result = c.post_care_nurse_config('16412345678', '123456', post_data, prod=4)
    # result = c.post_care_nurse_config_page('16412345678', '123456', page, prod=4)
    # result = c.del_care_nurse_config_ids('1', '16412345678', '123456', prod=4)
    # result = c.get_care_nurse_config_ids('2', '16412345678', '123456', prod=4)
    result = c.put_care_nurse_config_ids('2', '16412345678', '123456', post_data, prod=4)

    print(result)
    print(result.text)