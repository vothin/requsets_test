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
from common.recordlog import logs
from PIL import Image
import pytesseract

class Get_Code():

    def __init__(self, scene, prod=None):
        self.scene = scene
        self.pr = prod
        self.prod = 0

    def get_ncs_device_code(self):

        if self.pr == '10':
            self.prod += 7

        elif self.pr == '11':
            self.prod += 8

        elif self.pr == '12':
            self.prod += 9

        # 获得验证码
        c = Captcha_Base()
        response = c.get_captcha_base(self.scene, self.prod)
        logs.info(response)
        # logs.info(response.text)


        with open('../image/code/code.png', 'wb') as image:
            image.write(response.content)

        yanzhengmaImage = Image.open('../image/code/code.png')
        yanzhengmaCode = pytesseract.image_to_string(yanzhengmaImage).replace(" ", "")

        return yanzhengmaCode




if __name__ == '__main__':
    g = Get_Code('LOGIN', '10')
    g.get_ncs_device_code()


