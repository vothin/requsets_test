# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: care_member_relation.py
    @time: 2019/11/22 15:11
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Care_Member_Relation(Requests_Test):


    # 请求添加家人
    def post_care_member_relation(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 根据手机号查询家人信息
    def get_care_member_relation_getRelativeMemberByMobile(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_getRelativeMemberByMobile')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 获取等待通过列表
    def get_care_member_relation_getWaitPassList(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_getWaitPassList')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 查询家庭管理列表-谁能看我
    def post_care_member_relation_page(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_page')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 查询家庭管理列表-我能看谁
    def post_care_member_relation_page1(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_page1')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 发送下载app短信
    def post_care_member_relation_sendDownAPPSms(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_sendDownAPPSms')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 设置是否通过家人请求
    def put_care_member_relation_setPassed(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_setPassed')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 删除家庭管理
    def del_care_member_relation_ids(self, ids, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_ids')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 查询一个家庭管理
    def get_care_member_relation_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



    # 修改家庭管理
    def put_care_member_relation_id(self, id, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Care', 'care_member_relation_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test headers:%s' % gu[0])
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)




if __name__ == '__main__':
    c = Care_Member_Relation()

    post_data = {
        'memberId' : '4473',
        'relative_memberid' : '2247',
        'relation_name' : 'guanxi',
        'bool_vital_sign' : 'True',
        'bool_doctor_advice' : 'True',
        'bool_health_advert' : 'False',
        'bool_diagnosis' : 'False',
        'passed' : '1'
    }

    page_data = {
        'page_no': '1',
        'page_size': '10'
    }

    get_data = {'mobile' : '13412345678'}


    put_data = {
        'id' : '20',
        'passed' : '1'
    }

    # result = c.post_care_member_relation('13412345678', '123456', post_data)
    # result = c.get_care_member_relation_getRelativeMemberByMobile('13412345678', '123456', get_data)
    # result = c.get_care_member_relation_getWaitPassList('13412345678', '123456')
    # result = c.post_care_member_relation_page('13412345678', '123456', page_data)
    # result = c.post_care_member_relation_page1('13412345678', '123456', page_data)
    # result = c.put_care_member_relation_setPassed('13412345678', '123456', put_data)
    # result = c.del_care_member_relation_ids('1', '13412345678', '123456')
    result = c.get_care_member_relation_id('4', '13412345678', '123456')

    print(result)
    print(result.text)