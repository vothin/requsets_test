# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_vital_signs_setting.py
    @time: 2019/11/27 16:45
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Vital_Signs_Setting(Requests_Test):

    # 添加生命体征警告设置
    def post_care_vital_signs_setting(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_setting')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询生命体征警告设置列表(不分页)
    def post_care_vital_signs_setting_getList(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_setting_getList')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询生命体征类别列表
    def post_care_vital_signs_setting_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_setting_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询用户体征告警设置
    def get_care_vital_signs_setting_setting(self, memberId, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_setting_setting')
        self.suffix = self.suffix.format(memberId)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 删除生命体征类别
    def del_care_vital_signs_setting_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_setting_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个生命体征类别
    def get_care_vital_signs_setting_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_setting_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_Vital_Signs_Setting()


    post_data = {
        'group_id' : '9',
        'group_name' : 'mingzi',
        'param_id' : '9',
        'min_value' : '9',
        'max_value' : '19',
        'member_id' : '2247'
    }

    post_data2 = {
        'page_no' : '1',
        'page_size' : '10'
    }

    # result = c.post_care_vital_signs_setting('13412345678', '123456')
    # result = c.post_care_vital_signs_setting_getList('13412345678', '123456')
    # result = c.post_care_vital_signs_setting_page('13412345678', '123456', post_data2)
    # result = c.get_care_vital_signs_setting_setting('2247', '13412345678', '123456')
    # result = c.del_care_vital_signs_setting_ids('211', '13412345678', '123456')
    result = c.get_care_vital_signs_setting_id('210', '13412345678', '123456')
    print(result)
    print(result.text)
