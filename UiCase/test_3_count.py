from ddt import ddt,data,unpack
import unittest
from public import base
from oper import read_Config
from oper import read_excel
testcasefile = 'test_data.xlsx'
count = read_excel.XLDatainfo.get_sheet_data(testcasefile,'count')
count1 = read_excel.XLDatainfo.get_sheet_data(testcasefile,'count1')

@ddt
class Test_Count(unittest.TestCase):
    '''各查询页面'''
    def setUp(self) :
         self.url1 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForRegularEarnings'
        # self.url2 = 'https://api.haitoutech.com/haitou-order/assetsStatistic/queryAssetsStatisticsForAll'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'
         self.host = read_Config.ReadConfig().get_config_str('HOST','host')

    @data(*count)
    @unpack
    def test1(self,case_des,host,doc,type,code,result,clt,doc1,login):
        print('测试开始！')
        url = ''.join([self.host, doc])
        par = {'clt':clt,'token':base.get_token_ok(doc1,login)}
        r = base.method(url,method=type,data=par)
        #resp = r.json()
        print(r)
        #self.assertTrue(resp[code] == result)
        self.assertEqual(r[code],result,msg= '返回值错误')
        print('测试完成！')
    @data(*count1)
    @unpack
    def test2(self,case_des,host,doc,type,code,result,clt,token):
        print('测试开始！')
        url = ''.join([self.host, doc])
        par = {'clt':clt,'token':token}
        r = base.method(url,method=type,data=par)
        #resp = r.json()
        print(r)
        #self.assertTrue(resp[code] == result)
        self.assertEqual(r[code],result,msg= '返回值错误')
        print('测试完成！')
    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()