#!/usr/bin/env python

# encoding: utf-8
'''
    @author: Vothin
    @software: 自动化测试
    @file: recordlog.py
    @time: 2019/10/31 11:14
    @desc:
'''
# ********************************************************


import logging, os
import colorlog
from base.global_path import log_path

def record_logging(loggpath=None):

    color_logs = {
        'DEBUG':'cyan',
        'INFO':'green',
        'WARNING':'yellow',
        'ERROR':'red',
        'CRITICAL':'red',
    }

    if loggpath != None:
        loggpath = loggpath
    else:
        loggpath = log_path


    # 实例loggers
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # 设置日志级别

        # 日志存储在指定文件中
        fh = logging.FileHandler(loggpath, encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 日志打印在屏幕
        sh = colorlog.StreamHandler()   # 控制台日志输出颜色
        sh.setLevel(logging.DEBUG)

        formt = colorlog.ColoredFormatter('%(log_color)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                                           log_colors=color_logs)

        fh.setFormatter(formt)
        sh.setFormatter(formt)

        # 给logger对象添加handler
        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger

logs = record_logging()


if __name__ == '__main__':
    logs.info('English')
    logs.info('中文')


