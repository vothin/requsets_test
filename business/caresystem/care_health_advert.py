# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_health_advert.py
    @time: 2019/11/22 10:29
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Care_Health_Advert(Requests_Test):

    # 查询健康宣教列表
    def post_care_health_advert_page(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_health_advert_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 查询一个健康宣教
    def get_care_health_advert(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_health_advert')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    c = Care_Health_Advert()

    post_data = {
        'page_no' : '1',
        'page_size' : '10'
    }

    result = c.post_care_health_advert_page('13412345678', '123456', post_data)
    # result = c.get_care_health_advert('88', '13412345678', '123456')
    print(result)
    print(result.text)