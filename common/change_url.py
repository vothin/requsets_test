# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: change_url.py
    @time: 2019/11/4 11:17
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.recordlog import logs


class Change_URL(Requests_Test):

    keys_dict = []
    values_dict  = []
    url_kwargs = ''


    # 将参数字典拆分，拼接成url
    def get_url_kwargs(self, **kwargs):
        if kwargs != None:
            logs.info('get url_kwargs')

            # 或者kwargs的key和value
            keys = kwargs['data'].keys()
            values = kwargs['data'].values()

            for i in keys:
                self.keys_dict.append(i)

            for i in values:
                self.values_dict.append(i)

            for i in range(len(kwargs['data'])):
                self.url_kwargs += (self.keys_dict[i] + '=' + self.values_dict[i] + '&')

            return self.url_kwargs

        else:
            logs.info('not found kwargs')





if __name__ == '__main__':

    t = '6'
    t2 =    '7'
    suffix = '/goods/{}/area/{}'
    data = {
        'baidu': 'baidu',
        'bilibili': 'bilibili',
        'youku': 'youku'
    }

    c = Change_URL()