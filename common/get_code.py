# -*- coding:utf-8 -*-

'''
    @author: Vothin
    @software: 自动化测试
    @file: get_code.py
    @time: 2019/12/10 16:31
    @desc:
'''
# ********************************************************


from business.base.captcha_base import Captcha_Base
from PIL import Image
import pytesseract

class Get_Code():

    def __init__(self, scene, prod=None):
        self.scene = scene
        self.prod = prod

    def get_ncs_device_code(self):

        # 获得验证码
        c = Captcha_Base()
        response = c.get_captcha_base(self.scene, self.prod)

        # with open('../image/code/code.png', 'wd') as image:
        #     image.write(response.text)


if __name__ == '__main__':
    g = Get_Code('LOGIN', '7')
    g.get_ncs_device_code()
