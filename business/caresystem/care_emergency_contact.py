# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @qq: 757161350
    @mailbox: zy757161350@qq.com
    @file: care_emergency_contact.py
    @time: 2020/6/22 15:00
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Emergency_contact(Requests_Test):

    # 添加工作人员
    def post_care_emergency_contact(self, username=None, password=None, data=None, prod=None, json=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_emergency_contact')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)


if __name__ == '__main__':

    post_data = {
        'member_id' : '50216',
        'contact_name' : '新疆休养所',
        'mobile' : '09914512774'
    }

    c = Care_Emergency_contact()
    result = c.post_care_emergency_contact('13119003021', '123456', post_data, prod=2)