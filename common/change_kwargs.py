# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: change_kwargs.py
    @time: 2019/11/4 11:17
    @desc:
'''
# ********************************************************


from common.recordlog import logs


class Change_Kwargs():

    def __init__(self, kwargs):
        self.keys_dict = []
        self.values_dict  = []
        self.url_kwargs = ''
        self.kwargs = kwargs


    # 将参数字典拆分，拼接成url
    def get_kwargs(self):
        if self.kwargs != None:
            logs.info('get url_kwargs')
            # 或者kwargs的key和value
            keys = self.kwargs.keys()
            values = self.kwargs.values()

            for i in keys:
                self.keys_dict.append(i)

            for i in values:
                self.values_dict.append(i)

            for i in range(len(self.kwargs)):
                self.url_kwargs += (self.keys_dict[i] + '=' + str(self.values_dict[i]) + '&')

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

    c = Change_Kwargs(data)
    c.get_kwargs()