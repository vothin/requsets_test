# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_receipt.py
    @time: 2019/11/19 17:41
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Member_Receipt(Requests_Test):

    # 查询当前会员发票列表
    def get_member_receipt(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_receipt')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 添加会员增值税普通发票
    def post_member_receipt_ordinary(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   receipt_title          发票抬头
                        receipt_content        发票内容
                        tax_no                 发票税号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_receipt_ordinary')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 删除会员发票
    def del_member_receipt(self, id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   id         要删除的会员发票主键
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_receipt_del')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 设置会员发票为默认
    def put_member_receipt_default(self, id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   id                 要删除的会员发票主键
                        receipt_type       枚举，ELECTRO:电子普通发票，
                                                VATORDINARY：增值税普通发票，
                                                VATOSPECIAL：增值税专用发票,
                                           可用值:ELECTRO,VATORDINARY,VATOSPECIAL
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_receipt_default')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)




    # 修改会员增值税普通发票
    def put_member_receipt_ordinary(self, id, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   id                     要删除的会员发票主键
                        receipt_title          发票抬头
                        receipt_content        发票内容
                        tax_no                 发票税号
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_receipt_ordinary')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)




    # 根据订单sn查询订单发票信息
    def get_member_receipt_orderSn(self, order_sn, username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   order_sn            订单sn
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_receipt_orderSn')
        self.suffix = self.suffix.format(order_sn)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Receipt()


    post_data = {
        'receipt_title' : 'taitou',
        'receipt_content' : 'neirong',
        'tax_no' : 'shuihao'
    }

    result = m.get_member_receipt('13412345678', '123456')
    # result = m.post_member_receipt_ordinary('13412345678', '123456', post_data)
    # result = m.del_member_receipt('31', '13412345678', '123456')

    print(result)
    print(result.text)