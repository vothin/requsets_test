# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: get_md5.py
    @time: 2019/11/1 11:10
    @desc:
'''
# ********************************************************

import hashlib

def change_md5(password):
    '''转换成md5形式'''
    h = hashlib.md5()
    h.update(password.encode('utf-8'))
    h = h.hexdigest()
    return h

if __name__ == '__main__':
    p = change_md5('123456')

