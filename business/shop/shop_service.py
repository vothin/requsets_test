# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: shop_service.py
    @time: 2019/11/7 10:51
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs


class Shop_Service(Requests_Test):

    # 添加店铺服务绑定
    def post_shop_mapping(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  id              主键
                        nodeId          结点shopId
                        serviceId       serviceId
                        recommendOrder  推荐优先
        '''
        self.suffix = self.c.get_value('Shop', 'shop_service_mapping')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 删除店铺服务绑定
    def del_shop_mapping(self, ids, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  ids             要删除的店铺服务绑定主键集合
        '''
        self.suffix = self.c.get_value('Shop', 'shop_service_mapping_del')
        self.suffix = self.suffix.format(ids)
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.del_requests(self.url, gu[0])



    # 获取某个机构下的O2O店铺
    def post_shop_getShopId(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  shopId          shopId
                        page_no         页码
                        page_size       每页显示数量
        '''
        self.suffix = self.c.get_value('Shop', 'shop_service_getShopId')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



    # 获取某个机构下的O2O店铺--返回全部属性
    def post_shop_getShopIdAll(self, username=None, password=None, data=None, prod=None):
        '''
            相关参数有：  shopId          shopId
                        page_no         页码
                        page_size       每页显示数量
        '''
        self.suffix = self.c.get_value('Shop', 'shop_service_getShopIdAll')
        self.url = self.url_joint(prod)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        logs.info('Test interface:%s' % self.url)
        return self.post_requests(self.url, gu[0], gu[1])



if __name__ == '__main__':
    data = {
        'shopId' : '130',
        'page_no' : '10',
        'page_size' : '10'
    }

    s = Shop_Service()
    # result = s.post_shop_getShopId('13412345678', '123456', data)
    result = s.post_shop_getShopIdAll('13412345678', '123456', data)

    print(result)
    print('响应正文：', result.text)
    print('响应头：', result.headers)
    print('响应url：', result.url)
    print('响应对应请求方式：', result.request)
