# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
from public import base
from oper.read_Config import ReadConfig

@ddt
class Test_NumCount(unittest.TestCase):
    '''本年客户分析'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_BOSS', 'host_ican_boss_pc')
        self.doc = ReadConfig().get_config_str('HOST_BOSS', 'numcount')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test08_numcount(self):
        '''本年客户分析'''
        resp = requests.get(self.url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()