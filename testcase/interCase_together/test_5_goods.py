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
class Test_Goods(unittest.TestCase):
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

    def test04_goods(self):
        '''农资列表'''
        doc = "/goods/105710052/list/?page=1&size=10&curxname=&clscode=&clscode=&orderby="
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        # json_str = company.content.decode()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test05_goodscount(self):
        '''作物列表'''
        doc = "goods/105710052/?curxname=&clscode=&clscode=&orderby="
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        # json_str = company.content.decode()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test06_goodstype(self):
        '''地块数量'''
        doc = "lands/filter/count_list/?land_name=&page=1&size=12&order_class=&cusId=&empId=&landAreas=&cropCode=&riskCode=&userType= "
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