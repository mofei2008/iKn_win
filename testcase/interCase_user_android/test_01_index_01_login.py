
# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
from public import base
from oper import read_Config
from oper import read_excel
# testcasefile = 'test_data.xlsx'
# product = read_excel.X
# LDatainfo.get_sheet_data(testcasefile,'product')
from oper.read_Config import ReadConfig


@ddt
class Test_Login(unittest.TestCase):
    '''登录功能'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_USER_ANDROID', 'host_ican_user_android')
        self.doc = ReadConfig().get_config_str('HOST_USER_ANDROID', 'login')
        self.url = ''.join([self.host,self.doc])
        print(self.url)

    @data(['18610806332','Aa111111','httpCode',200])
    @unpack
    def test_login(self,username,password,code,result):
        '''登录功能'''
        print('测试开始！')
        par = {"username": username, "password": password}
        resp = base.method(self.url,method='post',data=par)
        r = resp.json()
        code = r[code]
        print(r)
        self.assertEqual(code,result,msg= '返回值错误')
        print('测试完成！')

    def tearDown(self):
        pass