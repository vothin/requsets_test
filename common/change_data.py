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


class Change_Data():

    def __init__(self, data, tail):
        self.data = data
        self.tail = tail


    def get_data(self):
        logs.info('get url_data')

        # 合并两个字典
        url_data = {
            **self.data,
            **self.tail
        }

        return url_data

    # # 将参数字典拆分，拼接成url
    # def get_kwargs(self):
    #     if self.kwargs != None:
    #         logs.info('get url_kwargs')
    #         # 或者kwargs的key和value
    #         keys = self.kwargs.keys()
    #         values = self.kwargs.values()
    #
    #         for i in keys:
    #             self.keys_dict.append(i)
    #
    #         for i in values:
    #             self.values_dict.append(i)
    #
    #         for i in range(len(self.kwargs)):
    #             self.url_kwargs += (self.keys_dict[i] + '=' + str(self.values_dict[i]) + '&')
    #
    #         return self.url_kwargs
    #
    #     else:
    #         logs.info('not found kwargs')





if __name__ == '__main__':

    t = '6'
    t2 =    '7'
    suffix = '/goods/{}/area/{}'
    data = {
        'baidu': 'baidu',
        'bilibili': 'bilibili',
        'youku': 'youku'
    }

    data2 = {
        'baidu1': 'baidu1',
        'bilibili1': 'bilibili1',
        'youku1': 'youku1'
    }

    c = Change_Data(data, data2)
    result = c.get_data()
    print(result)