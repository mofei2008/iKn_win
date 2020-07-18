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

@ddt
class Test_Index(unittest.TestCase):
    def setUp(self) :
        self.host = 'https://pbsapi.aikenong.com.cn/boss/'
        self.token = base.get_token_akn()
        self.header = {'Authorization': "JWT " + self.token}

    @data(['13611112222','akn2019666','httpCode',200],['13611112222','akn2019666','msg','登录成功'],['13611112222','2121212','code',["400"]])
    @unpack
    def test01_login(self,username,password,code,result):
        '''登录测试'''
        print('测试开始！')
        doc = "login/"
        url = ''.join([self.host,doc])
        par = {"username": username, "password": password}
        resp = base.method(url,method='post',data=par)
        # print(resp)
        code1 = resp[code]
        print(code1)
        print(resp)
        self.assertEqual(code1,result,msg= '返回值错误')
        print('测试完成！')

    def test02_company(self):
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


    def test03_info(self):
        doc = "user/informations/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        # json_str = company.content.decode()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test04_goods(self):
        '''农资总览'''
        doc = "goods/105710052/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test05_weather(self):
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

    def test06_lands(self):
        '''地块信息'''
        doc = "scattergram/lands/?dtype=custom"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test07_landcount(self):
        '''地块总览'''
        doc = "emp/landcount/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test08_numcount(self):
        '''本年客户分析'''
        doc = "custom/numcount/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')


    def test09_salerank(self):
        '''业绩榜'''
        doc = "emp/salerank/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test10_reduce(self):
        doc = "/yield/reduce"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test11_cuscount(self):
        '''客户排行榜'''
        doc = "emp/cuscount/"
        url = ''.join([self.host,doc])
        print(url)
        resp = requests.get(url, headers=self.header)
        json_str = resp.json()
        print(resp)
        print(json_str)
        code = resp.status_code
        self.assertEqual(code,200,msg= '返回值错误')

    def test12_mouthsale(self):
        '''月农资销售额'''
        doc = "goods/mouthsale/?m_date=2020-07"
        url = ''.join([self.host, doc])
        print(url)
        company = requests.get(url, headers=self.header)
        json_str = company.content.decode()
        print(company)
        print(json_str)
        code = company.status_code
        self.assertEqual(code, 200, msg='返回值错误')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()