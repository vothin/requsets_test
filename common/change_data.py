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



if __name__ == '__main__':

    t = '6'
    t2 =    '7'
    suffix = '/goods/{}/area/{}'
    data = {
        'baidu': 'baidu',
        'bilibili': 'bilibili',
        'youku': 'youku'
    }

    c = Change_Data(data, data)
    c.get_data()