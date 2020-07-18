import requests
import unittest

class TokenClass(unittest.TestCase):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json;charset=UTF-8',
                        'User-Agent': '*****',
                        'Accept-Version': '**'}
        self.url = 'https://api.haitoutech.com/'

    def getToken(self):
        data1 = {'email':'lidetao@163.com','password':'Aa111111','userType':'1','clt':'h5Wealth'}

        self.r = requests.post(url = 'https://api.haitoutech.com/haitou-user/user/loginByEmail', data=data1)
        print(self.r.json())
        token = self.r.json()['data']
        print(token)
        # return {'token'}

    def test_getInfo(self):
        self.getToken()
        self.r = requests.get(self.url + 'haitou-order/assetsStatistic/queryAssetsStatisticsForRegularEarnings', json=self.getToken(), headers=self.headers)
        # print( self.r.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    TokenClass().test_getInfo()