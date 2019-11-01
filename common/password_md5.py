# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: password_md5.py
    @time: 2019/11/1 11:10
    @desc:
'''
# ********************************************************

import hashlib

def pwd_md5(password):
    h = hashlib.md5()
    h.update(password.encode('utf-8'))
    h = h.hexdigest()
    return h

if __name__ == '__main__':
    p = pwd_md5('123456')

