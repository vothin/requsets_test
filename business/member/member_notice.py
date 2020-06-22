# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_notice.py
    @time: 2019/11/19 15:21
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Notice(Requests_Test):

    # 查询会员站内消息历史列表
    def get_member_nocice_logs(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   page_no             页码
                        page_size           每页显示数量
                        read                是否已读，1已读，0未读,可用值:0,1
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_nocice_logs')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 删除会员站内消息历史
    def del_member_nocice_logs_ids(self, ids, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   ids        要删除的消息主键
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_nocice_logs_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 将消息设置为已读
    def put_member_nocice_logs_ids(self, ids, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   ids        要设置为已读消息的id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_nocice_logs_read')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Notice()
    # result = m.get_member_nocice_logs('13412345678', '123456')
    # result = m.del_member_nocice_logs_ids('858', '13412345678', '123456')
    result = m.put_member_nocice_logs_ids('859', '13412345678', '123456')

    print(result)
    print(result.text)