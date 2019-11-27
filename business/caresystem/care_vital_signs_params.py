# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_vital_signs_params.py
    @time: 2019/11/27 14:46
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Vital_Signs_Params(Requests_Test):

    # 添加生命体征类别参数
    def post_care_vital_signs_params(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_params')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询生命体征类别参数列表
    def post_care_vital_signs_params_page(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_params_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 删除生命体征类别参数
    def del_care_vital_signs_params_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_params_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个生命体征类别参数
    def get_care_vital_signs_params_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_params_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改生命体征类别参数
    def put_care_vital_signs_params_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_params_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_Vital_Signs_Params()

    post_data = {
        'group_id' : '19',
        'group_name' : 'zuming',
        'min_limit_start' : '19',
        'min_limit_stand' : '30',
        'min_limit_end' : '49',
        'max_limit_start' : '30',
        'max_limit_stand' : '50',
        'max_limit_end' : '70',
        'input_type' : 'float',
        'param_name' : 'canshuming'
    }


    post_data1 = {
        'page_no' : '1',
        'page_size' : '10'
    }

    put_data = {'group_id' : '7'}

    # result = c.post_care_vital_signs_params('13412345678', '123456', post_data)
    # result = c.post_care_vital_signs_params_page('13412345678', '123456', post_data1)
    # result = c.del_care_vital_signs_params_ids('26', '13412345678', '123456')
    # result = c.get_care_vital_signs_params_id('24', '13412345678', '123456')
    result = c.put_care_vital_signs_params_id('24', '13412345678', '123456', put_data)
    print(result)
    print(result.text)
