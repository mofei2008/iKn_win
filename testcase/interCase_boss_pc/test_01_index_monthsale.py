# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
from public import base
from oper.read_Config import ReadConfig

@ddt
class Test_MonthSale(unittest.TestCase):
    '''月农资销售额'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_BOSS', 'host_ican_boss_pc')
        self.doc = ReadConfig().get_config_str('HOST_BOSS', 'monthsale')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test01_monthsale(self):
        '''月农资销售额'''
        company = requests.get(self.url, headers=self.header)
        json_str = company.content.decode()
        print(company)
        print(json_str)
        code = company.status_code
        self.assertEqual(code, 200, msg='返回值错误')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()