# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: member_address.py
    @time: 2019/11/11 15:36
    @desc:
'''
# ********************************************************


from common.recordlog import logs
from common.change_param import Change_Param
from common.requests_test import Requests_Test


class Member_Address(Requests_Test):

    # 添加会员地址
    def post_member_address(self, username=None, password=None, data=None, prod=None, region=None):
        '''
            相关参数有:   name                        收货人姓名
                        addr                        详细地址
                        tel                         联系电话(一般指座机)
                        mobile                      手机号码
                        def_addr                    是否为默认收货地址,1为默认
                        ship_address_name           地址别名
                        region                      地区，拼在url后面
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_address')
        if region:
            url = ''
            keys_list = []
            valuse_list = []

            # 获得字典的key
            for i in region.keys():
                keys_list.append(i)

            # 获得字典的value
            for i in region.values():
                valuse_list.append(i)

            # 拼成url
            for i in range(len(region)):
                url += '&' + keys_list[i] + '=' + valuse_list[i]

            self.url = self.url_joint(prod) + gu[1] + url
        else:
            self.url = self.url_joint(prod) + gu[1]

        logs.info('test url:%s' % self.url)

        return self.post_requests(self.url, gu[0], data)



    # 查询当前会员的某个地址
    def get_member_address_id(self, id,  username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  id          要查询的地址id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_address_id')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)


    # 修改会员地址
    def put_member_address_id(self, id,  username=None, password=None, data=None, prod=None, region=None):
        '''
            相关参数有:   id                      主键
                        name                    收货人姓名
                        addr                    详细地址
                        tel                     联系电话(一般指座机)
                        mobile                  手机号码
                        def_addr                是否为默认收货地址,1为默认
                        ship_address_name       地址别名
                        region                  地区，拼在url后面
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_address_id_put')
        self.suffix = self.suffix.format(id)

        # 判断是否有地址
        if region:
            url = ''
            keys_list = []
            valuse_list = []

            # 获得字典的key
            for i in region.keys():
                keys_list.append(i)

            # 获得字典的value
            for i in region.values():
                valuse_list.append(i)

            # 拼成url
            for i in range(len(region)):
                url += '&' + keys_list[i] + '=' + valuse_list[i]

            self.url = self.url_joint(prod) + gu[1] + url
        else:
            self.url = self.url_joint(prod) + gu[1]

        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 删除会员地址
    def del_member_address_id(self, id,  username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   id                      要删除的会员地址id
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_address_id_del')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.del_requests(self.url, gu[0], data)



    # 设置地址为默认
    def put_member_address_id_default(self, id,  username=None, password=None, data=None, prod=None):
        '''
            相关参数有:   id        主键
        '''

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_address_id_default_put')
        self.suffix = self.suffix.format(id)
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.put_requests(self.url, gu[0], data)



    # 查询当前会员地址列表
    def get_member_addresses(self, username=None, password=None, data=None, prod=None):

        # 调用Change_Param类
        cu = Change_Param(username, password, prod)
        gu = cu.get_params()

        # 拼接url
        self.suffix = self.c.get_value('Member', 'members_addresses')
        self.url = self.url_joint(prod) + gu[1]
        logs.info('test url:%s' % self.url)

        return self.get_requests(self.url, gu[0], data)



if __name__ == '__main__':
    m = Member_Address()

    address = {
        'name' : 'test',
        'addr' : 'dizhi',
        'tel'  : 'dianhua',
        'mobile' : '13412345678',
        'def_addr' : '0',
        'ship_address_name' : 'bieming',

        'region.provinceId' : '18',
        'region.province': '湖南',

        'region.cityId': '1482',
        'region.city': '长沙市',

        'region.countyId' : '48941',
        'region.county' : '浏阳市',

        'region.townId': '52588',
        'region.town' : '城区',

        'region.ship_address_name': 'bieming',
    }

    region = {
        'province_id' : '18',
        'province': '湖南',

        'city_id': '1482',
        'city': '长沙市',

        'county_id' : '48941',
        'county' : '浏阳市',

        'town_id': '52588',
        'town' : '城区'
    }

    # result = m.post_member_address('13412345678', '123456', address, region=region)
    # result = m.get_member_address_id('2247', '13412345678', '123456')
    result = m.put_member_address_id('65346', '13412345678', '123456', address, prod=3, region=region)

    print(result)
    print(result.text)
    print(result.url)


