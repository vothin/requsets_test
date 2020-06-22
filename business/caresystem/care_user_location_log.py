# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_user_location_log.py
    @time: 2019/11/22 14:56
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Care_User_Location_Log(Requests_Test):

    # 查询地理位置信息列表
    def post_care_user_location_log(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_user_location_log')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


if __name__ == '__main__':
    c = Care_User_Location_Log()

    post_data = {
        'page_no' : '1',
        'page_size' : '10'
    }

    result = c.post_care_user_location_log('13412345678', '123456', post_data)

    print(result)
    print(result.text)