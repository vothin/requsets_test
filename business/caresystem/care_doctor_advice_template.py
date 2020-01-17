# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @qq: 757161350
    @mailbox: zy757161350@qq.com
    @software: 自动化测试
    @file: care_doctor_advice_template.py
    @time: 2020/1/10 9:37
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Doctor_Advice_Template(Requests_Test):

    # 添加医嘱常用语
    def post_care_doctor_advice_template(self, username=None, password=None, data=None, prod=None, json=None):
        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_doctor_advice_template')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



if __name__ == '__main__':
    c = Care_Doctor_Advice_Template()

    post_data = {
        'detail' : '内容'
    }

    result = c.post_care_doctor_advice_template('16412345678', '123456', post_data, prod=4)

    print(result)
    print(result.text)