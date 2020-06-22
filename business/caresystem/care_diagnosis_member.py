# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_diagnosis_member.py
    @time: 2019/11/25 11:21
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Diagnosis_Member(Requests_Test):

    # 查询医生最近一周问诊列表(不分页)
    def post_care_diagnosis_member_getWeekList(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_diagnosis_member_getWeekList')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_Diagnosis_Member()

    result = c.post_care_diagnosis_member_getWeekList('13412345678', '123456', prod=6)
    print(result)
    print(result.text)
