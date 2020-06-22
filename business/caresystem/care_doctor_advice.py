# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_doctor_advice.py
    @time: 2019/11/22 10:56
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_Doctor_Advice(Requests_Test):

    # 查询医嘱列表
    def post_care_doctor_advice_page(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_doctor_advice_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_Doctor_Advice()

    post_data = {
        'page_no' : '1',
        'page_size' : '10',
        'doctorid' : '56'
    }

    result = c.post_care_doctor_advice_page('13412345678', '123456')

    print(result)
    print(result.text)