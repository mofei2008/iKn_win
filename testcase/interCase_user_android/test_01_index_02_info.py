# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
import json
from public import base
# from oper import read_Config
# from oper import read_excel
# testcasefile = 'test_data.xlsx'
# product = read_excel.XLDatainfo.get_sheet_data(testcasefile,'product')
from oper.read_Config import ReadConfig


@ddt
class Test_UserInfo(unittest.TestCase):
    '''用户信息'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_USER_ANDROID', 'host_ican_user_android')
        self.doc = ReadConfig().get_config_str('HOST_USER_ANDROID', 'user_info')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn_android()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test01_userinfo(self):
        '''用户信息'''
        resp = base.method(self.url,method='get',headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()