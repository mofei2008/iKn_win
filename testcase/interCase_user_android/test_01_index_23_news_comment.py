# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
from public import base
from oper import read_Config
from oper import read_excel

from oper.read_Config import ReadConfig

@ddt
class Test_Registration(unittest.TestCase):
    '''新闻详情'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_USER_ANDROID', 'host_ican_user_android')
        self.doc = ReadConfig().get_config_str('HOST_USER_ANDROID', 'news_comment')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn_android()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test01_registration(self):
        '''新闻详情'''
        resp = base.method(self.url,method='get',headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def tearDown(self):
        pass