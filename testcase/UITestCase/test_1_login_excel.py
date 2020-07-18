#coding=utf-8
#!usr/bin/python
import unittest
from ddt import ddt,data,unpack
from public import base
from log.log import UserLog
from oper.read_Config import ReadConfig
from oper import read_excel,read_Db_records
# testcasefile = 'test_data.xlsx'
# login = read_excel.XLDatainfo.get_sheet_data(testcasefile,'login')
login_data = read_Db_records.db_read('login')
print()
@ddt
class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    '''登录功能'''
    def setUp(self) :
        print('测试开始！')
        self.logger.debug('日志打印开始')
        self.host = ReadConfig().get_config_str('HOST','host')
        print(type(self.host))
    @data(*login_data)
    @unpack
    def test1(self,id,case_des,doc,code,result,method_type,par):
        host = self.host
        url = ''.join([host, doc])
        print(url)
        par = eval(par)
        print(par)
        print(type(par))
        # print(data)
        r = base.method(url,method_type,data=par)
        self.assertTrue(r[code] == result)
        print(r)
        print('测试完成！')
    @classmethod
    def tearDownClass(cls):
        cls.log.Close_handle()
    def tearDown(self):
        pass