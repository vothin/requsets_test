#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: global_path.py
    @time: 2019/10/31 10:24
    @desc:
'''
# ********************************************************

import os, sys

BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)

url_path = os.path.join(BIR, r'config\url.ini')
log_path = os.path.join(BIR, r'log\log.log')

