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
class Test_Price(unittest.TestCase):
    '''地块任务'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_USER_ANDROID', 'host_ican_user_android')
        self.doc = ReadConfig().get_config_str('HOST_USER_ANDROID', 'apply')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn_android()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test01_price(self):
        '''地块任务'''
        par = {'land_ids':'41547','link_name': '22222',"link_tel":"34124132","msg":"jjjj","rs_crop" : '水稻',"sensing_type_code":"3"}
        resp = base.method(self.url,method='post',headers=self.header,data=par)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def tearDown(self):
        pass
