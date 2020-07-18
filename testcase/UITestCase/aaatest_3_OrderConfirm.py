from ddt import ddt,data,unpack
#sys.path.append('./test_case')
import unittest
#from public import HttpService
from public import base
import requests

testcasefile = 'test_data.xlsx'
order1 = base.get_sheet_data(testcasefile,'order1')

@ddt
class Test_Order_Confirm(unittest.TestCase):
    '''订单确认页'''
    def setUp(self) :
         self.url1 = 'https://api.haitoutech.com/haitou-order/order/confirmOrderInfo'
         # self.url2 = 'https://api.haitoutech.com//haitou-order/rechargeOrder/generateRechargeOrder'
        # self.url3 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserSetting'
        # self.url4 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryUserAccount'
        # self.url5 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryOrderList'
        # self.url6 = 'https://api.haitoutech.com/haitou-order/moneyFund/queryAccountEarningsList'
        # self.url7 = 'https://api.haitoutech.com/haitou-user/userInfo/queryUserInfoForWealth'
    @data(*order1)
    @unpack
    def test2(self,case_des,host,doc,type,code,result,returnType,productType,orderAmount,clt,doc1,login):
        print('测试开始！')
        url = ''.join([host, doc])
        token = base.get_token_ok(doc1, login)
        a = token
        par = {'clt':clt,'returnType':returnType,'productType':productType,'token':token}
        # par = {'clt': 'h5Wealth', 'returnType': '151', 'productType': '340', 'token': '5c3fd464-d220-439f-a8c7-9ad624f30394'}
        resp = base.get_ProId(data=par)
        # print(resp)
        # dd = resp['data']
        # # print(dd)
        dd = resp['data'][3]['id']
        print(dd)
        par1 = {'clt':clt,'productId':dd,'orderAmount':orderAmount,'token':token}
        resp1 = base.method(url,method=type,data=par1)
        # print(resp1)
        self.assertEqual(resp1[code],result,msg= '返回值错误')
        print('测试完成！')

    def tearDown(self):
        pass
if __name__ =='__main__':
    unittest.main()