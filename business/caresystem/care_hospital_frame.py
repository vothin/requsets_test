# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_hospital_frame.py
    @time: 2020/1/3 16:09
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Care_Hospital_Frame(Requests_Test):

    # 添加医院结构
    def post_care_hospital_frame(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_hospital_frame')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询医院结构列表
    def post_care_hospital_frame_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_hospital_frame_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 删除医院结构
    def del_care_hospital_frame_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_hospital_frame_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个医院结构
    def get_care_hospital_frame_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_hospital_frame_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改医院结构
    def put_care_hospital_frame_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_hospital_frame_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)




if __name__ == '__main__':

    c = Care_Hospital_Frame()

    post_data = {
        'create_time' : '1578040031',
        'update_time' : '1578040031',
        'sync_time' : '1578040031',
        'type' : '2',
        'name' : 'chuang',
        'alias' : 'chuang',
        'parent_id' : '2'
    }

    page = {
        'page_no' : '1',
        'page_size' : '10'
    }

    # result = c.post_care_hospital_frame('16412345678', '123456', post_data, prod=4)
    # result = c.post_care_hospital_frame_page('16412345678', '123456', page, prod=4)
    result = c.del_care_hospital_frame_ids('112', '16412345678', '123456', prod=6)
    # result = c.get_care_hospital_frame_id('2', '16412345678', '123456', prod=4)
    # result = c.put_care_hospital_frame_id('2', '16412345678', '123456', post_data, prod=4)
    print(result)
    print(result.text)