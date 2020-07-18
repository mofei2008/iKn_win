# coding=utf-8
# !usr/bin/python
from ddt import ddt,data,unpack
import unittest
import requests
import json
from public import base
from oper.read_Config import ReadConfig

class Test_CropList(unittest.TestCase):
    '''作物列表'''
    def setUp(self) :
        self.host = ReadConfig().get_config_str('HOST_BOSS', 'host_ican_boss_pc')
        self.doc = ReadConfig().get_config_str('HOST_BOSS', 'croplist')
        self.url = ''.join([self.host,self.doc])
        self.token = base.get_token_akn()
        self.header = {'Authorization': "JWT " + self.token}
        print(self.url)

    def test05_crop_list(self):
        '''作物列表'''
        resp = requests.get(self.url, headers=self.header)
        json_str = resp.json()
        # json_str = company.content.decode()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')


    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()