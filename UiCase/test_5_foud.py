from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests
from log.log import UserLog
import json
from oper import read_Config
from oper import read_excel
testcasefile = 'test_data.xlsx'
foud = read_excel.XLDatainfo.get_sheet_data(testcasefile,'foud')

@ddt
class Test_Product(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    '''产品列表页'''
    def setUp(self) :
        # self.url1 = 'https://api.haitoutech.com/haitou-order/moneyFund/generateBuyOrder'
        self.logger.info('aaaadfdsafasdfsdaf')
        self.host = read_Config.ReadConfig().get_config_str('HOST','host')
        # self.url2 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForAll'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'
    @data(*foud)
    @unpack
    def test1(self,case_des,host,doc,type,code,result,orderAmount,clt,doc1,login):
        print('测试开始！')
        url = ''.join([self.host, doc])
        token = base.get_token_ok(doc1,login)
        print(token)
        par = {'clt': clt,'orderAmount': orderAmount,'token':token,'certificationUrl':base.upload_file(token)}
        print(par)
        resp = requests.post(url,data=par,verify=False).json()
        print(resp)
        dd = resp[code]
        print(dd)
        self.assertEqual(dd,result,msg= '返回值错误')
        print('测试完成！')
    @classmethod
    def tearDownClass(cls):
        cls.log.Close_handle()
    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()