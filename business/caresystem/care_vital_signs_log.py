# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_vital_signs_log.py
    @time: 2019/11/26 14:46
    @desc:
'''
# ********************************************************

import json
from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Care_Vital_Signs_Log(Requests_Test):

    # 批量添加生命体征日志
    def post_care_vital_signs_log(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_log')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 通过父级id删除生命体征日志
    def del_care_vital_signs_log_deleteByParentId(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_log_deleteByParentId')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询生命体征分组日志列表(不分页)
    def post_care_vital_signs_log_getGroupLogList(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_vital_signs_log')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)


if __name__ == '__main__':
    c = Care_Vital_Signs_Log()

    post_data = [
        {
            "group_id": 19,
            "member_id": 2247,
            "param_id": 19,
            "setting_id": 19,
            "vs_value": 99
        }
    ]


    del_data = {
        'parentid' : '2791'
    }


    # post_data = json.dumps(post_data)
    # print(post_data)

    # result = c.post_care_vital_signs_log('13412345678', '123456', json=post_data)
    result = c.del_care_vital_signs_log_deleteByParentId('13412345678', '123456', del_data)

    print(result)
    print(result.text)
    print(result.url)