# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: goods_search.py
    @time: 2019/11/1 9:55
    @desc:
'''
# ********************************************************

from common.requests_test import Requests_Test
from common.change_param import Change_Param
from common.recordlog import logs

class Goods_Search(Requests_Test):

    # 查询商品列表
    def get_goods_search(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  page_on     页码
                        page_size   每页数量
                        keyword     关键字
                        category    分类
                        brand       品牌
                        price       价格
                        sort        排序：关键字_排序,可用值:def_asc,def_desc,price_asc,price_desc,buynum_asc,buynum_desc,grade_asc,grade_desc
                        prop        属性:参数名_参数值@参数名_参数值
                        seller_id   卖家id，搜索店铺商品的时候使用
                        shop_cat_id 商家分组id，搜索店铺商品的时候使用
        '''

        self.suffix = self.c.get_value('Goods', 'goods_search')
        self.url = self.url_joint(prod)
        logs.info('Test interface:%s' % self.url)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        return self.get_requests(self.url, gu[0], gu[1])



    # 查询商品列表
    def get_goods_searchAllGoods(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  page_on     页码
                        page_size   每页数量
                        keyword     关键字
                        category    分类
                        brand       品牌
                        price       价格
                        sort        排序：关键字_排序,可用值:def_asc,def_desc,price_asc,price_desc,buynum_asc,buynum_desc,grade_asc,grade_desc
                        prop        属性:参数名_参数值@参数名_参数值
                        seller_id   卖家id，搜索店铺商品的时候使用
                        shop_cat_id 商家分组id，搜索店铺商品的时候使用
        '''

        self.suffix = self.c.get_value('Goods', 'goods_search_searchAllGoods')
        self.url = self.url_joint(prod)
        logs.info('Test interface:%s' % self.url)

        # 调用Change_Param类
        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        return self.get_requests(self.url, gu[0], gu[1])



    # # 查询商品选择器
    def get_goods_selector(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  page_on     页码
                        page_size   每页数量
                        keyword     关键字
                        category    分类
                        brand       品牌
                        price       价格
                        sort        排序：关键字_排序,可用值:def_asc,def_desc,price_asc,price_desc,buynum_asc,buynum_desc,grade_asc,grade_desc
                        prop        属性:参数名_参数值@参数名_参数值
                        seller_id   卖家id，搜索店铺商品的时候使用
                        shop_cat_id 商家分组id，搜索店铺商品的时候使用
        '''

        self.suffix = self.c.get_value('Goods', 'goods_search_selector')
        self.url = self.url_joint(prod)
        logs.info('Test interface:%s' % self.url)

        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        return self.get_requests(self.url, gu[0], gu[1])



    def get_goods_words(self, username=None, password=None, data=None, prod=False):
        '''
            相关参数有：  page_on     页码
                        page_size   每页数量
                        keyword     关键字
                        category    分类
                        brand       品牌
                        price       价格
                        sort        排序：关键字_排序,可用值:def_asc,def_desc,price_asc,price_desc,buynum_asc,buynum_desc,grade_asc,grade_desc
                        prop        属性:参数名_参数值@参数名_参数值
                        seller_id   卖家id，搜索店铺商品的时候使用
                        shop_cat_id 商家分组id，搜索店铺商品的时候使用
        '''

        self.suffix = self.c.get_value('Goods', 'goods_search_words')
        self.url = self.url_joint(prod)
        logs.info('Test interface:%s' % self.url)

        cu = Change_Param(username, password, data)
        gu = cu.get_params()

        return self.get_requests(self.url, gu[0], gu[1])



if __name__ == '__main__':
    data = {
        'page_on' : '1',
        'page_size' : '1',
        'category'  : '1'
    }

    g = Goods_Search()
    result = g.get_goods_search('13412345678', '123456', data=data)
    # result = g.get_goods_selector(data=data)
    # result = g.get_goods_searchAllGoods(data=data)
    print(result.text)