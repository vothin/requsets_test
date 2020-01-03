# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_employee.py
    @time: 2020/1/3 16:55
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Employee(Requests_Test):

    # 添加工作人员
    def post_care_employee(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_employee')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询工作人员列表
    def post_care_employee_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_employee_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 删除工作人员
    def del_care_employee_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_employee_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个工作人员
    def get_care_employee_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_employee_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改工作人员
    def put_care_employee_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_employee_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)


if __name__ == '__main__':
    c = Care_Employee()

    post_data = {
        'type' : '2',
        'name' : 'name',
        'create_time' : '1578042216',
        'update_time' : '1578042216',
        'sync_time' : '1578042216',
        'part_id' : '2',
        'sex' : '0',
        'age' : '11',
        'device_id' : '11'

    }

    page = {
        'page_no' : '1',
        'page_size' : '10'
    }

    # result = c.post_care_employee('16412345678', '123456', post_data, prod=4)
    # result = c.post_care_employee_page('16412345678', '123456', page, prod=4)
    # result = c.del_care_employee_ids('1', '16412345678', '123456', prod=4)
    # result = c.get_care_employee_ids('2', '16412345678', '123456', prod=4)
    result = c.put_care_employee_ids('2', '16412345678', '123456', post_data, prod=4)

    print(result)
    print(result.text)