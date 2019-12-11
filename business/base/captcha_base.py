# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: captcha_base.py
    @time: 2019/12/10 15:36
    @desc:
'''
# ********************************************************


from common.requests_test import Requests_Test
from common.recordlog import logs

class Captcha_Base(Requests_Test):

    # 生成验证码
    def get_captcha_base(self, scene, prod=None):
        self.suffix = self.c.get_value('Base', 'captcha_base')
        self.suffix = self.suffix.format('777', scene)
        logs.info(self.suffix)
        logs.info(prod)
        self.url = self.url_joint(prod)

        logs.info('url:%s' % self.url )
        return self.get_requests(self.url)


if __name__ == '__main__':
    c = Captcha_Base()
    result = c.get_captcha_base('LOGIN', prod=7)

    print(result)
    print(result.text)
