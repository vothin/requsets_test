# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_snapshot.py
    @time: 2019/11/11 10:34
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Goods_Snapshot(Requests_Test):

    # 查询一个交易快照
    def get_goods_snapshot(self, id, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Deal', 'goods_snapshots')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])


if __name__ == '__main__':
    g = Goods_Snapshot()
    result = g.get_goods_snapshot('16')
    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)