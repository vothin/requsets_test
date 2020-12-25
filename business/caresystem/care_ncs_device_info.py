# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_ncs_device_info.py
    @time: 2020/1/6 17:52
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test

class Care_Ncs_Nevice_Info(Requests_Test):

    # 添加设备信息
    def post_care_ncs_device_info(self, username=None, password=None, data=None, prod=None, json=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_ncs_device_info')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询设备信息列表
    def post_care_ncs_device_info_page(self, username=None, password=None, data=None, prod=None, json=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_ncs_device_info_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 删除设备信息
    def del_care_ncs_device_info_ids(self, ids, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_ncs_device_info_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 一个设备信息
    def get_care_ncs_device_info_ids(self, ids, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_ncs_device_info_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改设备信息
    def put_care_ncs_device_info_ids(self, ids, username=None, password=None, data=None, prod=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_ncs_device_info_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)


if __name__ == '__main__':
    c = Care_Ncs_Nevice_Info()

    post_data = {
        'sync_time': '3',
        'code': '3',
        'model': '3',
        'soft_ver': '3',
        'hard_ver': '3',
        'name': 'name',
        'eth_mac': '3',
        'eth_ip': '3',
        'wifi_mac': '3',
        'wifi_ip': '3',
        'wifi_hostname': '3',
        'room_num': '3',
        'room_id' : '3',
        'bed_num' : '3',
        'bed_name' : '3',
        'user_type' : '3',
        'user_id' : '3',
        'sip_ip' : '3',
        'sip_id' : '3',
        'sip_password' : '3',
        'sip_online' : '3',
        'sip_call_list' : '3',
        'sip_hosting_id' : '3',
        'ir_config' : '3'
    }

    page = {
        'page_no': '1',
        'page_size': '10'
    }

    # result = c.post_care_ncs_device_info('16412345678', '123456', post_data, prod=4)
    # result = c.post_care_ncs_device_info_page('16412345678', '123456', page, prod=4)
    # result = c.del_care_ncs_device_info_ids('1', '16412345678', '123456', prod=4)
    # result = c.get_care_ncs_device_info_ids('2', '16412345678', '123456', prod=4)
    # result = c.put_care_ncs_device_info_ids('2', '16412345678', '123456', prod=4)
    result = c.del_care_ncs_device_info_ids('164', '16412345678', '123456', prod=4)

    print(result)
    print(result.text)
