# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_comment_buyer.py
    @time: 2019/11/13 17:26
    @desc:
'''
# ********************************************************

import json
from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Comment(Requests_Test):

    # 查询我的评论列表
    def get_member_comments(self, username=None, password=None, data=None, prod=None):
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

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_comments')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 提交评论
    def post_member_comments(self, username=None, password=None, data=None, prod=None, json=None):
        '''
            相关参数有:   comment             评论动态评分vo
                            delivery_score              发货速度评分1-5
                            description_score           描述相符度评分1-5
                            order_sn                    订单编号
                            service_score               服务评分1-5
                            comments                    会员评论vo的list
                                grade                       好中差评,可用值:good,neutral,bad
                                sku_id                      会员评论商品规格id
                                content                     评论内容
                                images                      会员评论的图片
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_comments')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data, json)



    # 查询某商品的评论
    def get_member_comments_goods(self, goods_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   content             评论内容
                        goods_id            商品id
                        goods_name          商品名称
                        grade               好中差评
                        have_image          是否有图
                        keyword             模糊查询的关键字
                        member_id           会员id
                        member_name         会员名称
                        reply_status        回复状态
                        page_no             页码
                        page_size           分页数
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_comments_goods')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询某商品的评论
    def get_member_comments_count(self, goods_id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_comments_count')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


if __name__ == '__main__':
    m = Member_Comment()

    # post_data = {
    #     'comments' : [{
    #         'content' : 'pinglun',
    #         'grade' : 'good',
    #         'images' : [],
    #         'sku_id' : 0
    #     }],
    #     'delivery_score' : 5,
    #     'description_score' : 4,
    #     'order_sn' : '13',
    #     'service_score' : 3
    # }

    post_data = {
          "comments": [
            {
              "content": "1",
              "grade": "good",
              "images": [],
              "sku_id": 0
            }
          ],
          "delivery_score": 3,
          "description_score": 1,
          "order_sn": "123",
          "service_score": 1
    }

    get_data = {
        'page_no' : '1',
        'page_size' : '1'
    }

    # result = m.get_member_comments('13412345678', '123456')
    # result = m.post_member_comments('13412345678', '123456', post_data, )
    # result = m.post_member_comments('13412345678', '123456', json=post_data)
    result = m.get_member_comments_goods('340', '13412345678', '123456', get_data)
    # result = m.get_member_comments_count('340', '13412345678', '123456')
    print(result)
    print(result.text)


