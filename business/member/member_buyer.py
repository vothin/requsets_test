# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_buyer.py
    @time: 2019/11/13 12:19
    @desc:
'''
# ********************************************************

from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Buyer(Requests_Test):


    # 查询当前会员信息
    def get_member_buyer(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 完善会员细信息
    def put_member_buyer(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   nickname            昵称
                        sex                 会员性别,1为男，0为女
                        region              地区
                        birthday            会员生日
                        address             详细地址
                        email               邮箱
                        mobile              手机号码
                        tel                 座机号码
                        face                会员头像
                        tags                用户标签
                        boolDoctor          是否医生
                        doctorType          医生类型（内科医生，骨科医生等）
                        doctorAge           从业时间，单位年
                        doctorNo            医生执业编号
                        doctorIntroduction  医生简介(富文本)
                        worktime            上班时间
                        closingtime         下班时间
                        dayoff              单双休：0双休 1单休
                        age                 年龄
                        midentity           身份证号
        '''
        self.suffix = self.c.get_value('Member', 'members_buyer')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.put_requests(self.url, gu[0], gu[1])



    # SNS完善会员信息
    def put_member_buyer_editForSNS(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有:   mobile              手机号码
                        sex                 会员性别,1为男，0为女
                        age                 年龄
                        face                头像
                        nickname            用户昵称
                        intro               个人简介
        '''
        self.suffix = self.c.get_value('Member', 'members_buyer_editForSNS')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.put_requests(self.url, gu[0], gu[1])



    # 查询医生信息
    def get_member_buyer_getDoctor(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer_getDoctor')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 查询医生列表
    def get_member_buyer_getDoctorList(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer_getDoctorList')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 查询当前会员信息ForSNS
    def get_member_buyer_getForSNS(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer_getForSNS')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 根据手机号查询任意用户信息
    def get_member_buyer_getMemberByMobile(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer_getMemberByMobile')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])



    # 注销会员登录
    def post_member_buyer_logout(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer_logout')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 统计当前会员的一些数据
    def get_member_buyer_statistics(self, username=None, password=None, data=None, prod=False):
        self.suffix = self.c.get_value('Member', 'members_buyer_statistics')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.get_requests(self.url, gu[0], gu[1])

