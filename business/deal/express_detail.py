# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: express_detail.py
    @time: 2019/11/8 16:49
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Express_Detail(Requests_Test):

    # 查询物流详细
    def get_checkout_params(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  id          物流公司id
                        num         快递单号
        '''
        self.suffix = self.c.get_value('Deal', 'checkout_params')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])


if __name__ == '__main__':
    data = {
        'id' : '1',
        'num' : '1'
    }
    e = Express_Detail()
    result = e.get_checkout_params('13412345678', '123456', data)
    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)

