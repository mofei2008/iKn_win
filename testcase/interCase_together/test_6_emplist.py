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
# @ddt
class Test_Lands(unittest.TestCase):
    def setUp(self) :
        self.host = 'https://pbsapi.aikenong.com.cn/boss/'
        self.token = base.get_token_akn()
        self.header = {'Authorization': "JWT " + self.token}
    def test01_company(self):
        '''公司信息'''
        doc = "locations/company/"
        url = ''.join([self.host,doc])
        print(url)

        print(self.header)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test02_weather(self):
        '''天气预报'''
        doc = "wth/caiyun/?province=%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81&city=%E5%A4%A7%E5%BA%86%E5%B8%82&county=%E9%BE%99%E5%87%A4%E5%8C%BA"
        url = ''.join([self.host,doc])
        print(url)
        print(self.header)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test03_reduce(self):
        '''作物比例'''
        doc = "/yield/reduce"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test04_employee(self):
        '''员工列表'''
        doc = "/emp/list/105710052/?page=1&size=10"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
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