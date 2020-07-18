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
class Test_Visit_time(unittest.TestCase):
    '''注册接口开放'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_USER_ANDROID', 'host_ican_user_android')
        self.doc = ReadConfig().get_config_str('HOST_USER_ANDROID', 'visit_time')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn_android()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test01_visit_time(self):
        '''注册接口开放'''
        par = {'act_content':'查看地块列表','code' : 20,'start_time': 1594720545}

        resp = base.method(self.url,method='post',headers=self.header,data=par)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,201,msg= '返回值错误')

    def tearDown(self):
        pass
