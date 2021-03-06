# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_ask.py
    @time: 2019/11/13 11:23
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Ask(Requests_Test):

    # 查询我的咨询列表
    def get_member_asks(self, username=None, password=None, data=None, prod=None):
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
                        page_size           每页显示数量
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_asks')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 添加咨询
    def post_member_ask(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   ask_content                 咨询内容
                        goods_id                    咨询商品id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_asks')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)


    # 查询某商品的咨询
    def get_member_asks_goodsId(self, goods_id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   page_no             页码
                        page_size           每页显示数量
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_asks_goodsId')
        self.suffix = self.suffix.format(goods_id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Ask()

    get_data = {
        'page_no' : '1',
        'page_size' : '1'
    }

    post_data = {
        'ask_content' : 'xixunneirong',
        'goods_id' : '343'
    }



    # reslut = m.get_member_asks('13412345678', '123456')
    # reslut = m.post_member_ask('13412345678', '123456', data=post_data)
    reslut = m.get_member_asks_goodsId('343', '13412345678', '123456', get_data)


    print(reslut)
    print(reslut.text)




