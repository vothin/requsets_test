# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_comment_buyer.py
    @time: 2019/11/13 17:26
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Comment_Buyer(Requests_Test):

    # 查询我的评论列表
    def get_member_comments(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   content             评论内容
                        goods_id            商品id
                        goods_name          商品名称
                        grade               好中差评
                        have_image          是否有图
                        keyword             模糊查询的关键字
                        member_id           会员id
                        member_name         会员名称
                        page_no             页码
                        page_size           分页数
                        reply_status        回复状态
        '''
        self.suffix = self.c.get_value('Member', 'members_comments')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])