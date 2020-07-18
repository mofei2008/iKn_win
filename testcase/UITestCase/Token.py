import requests
import unittest

class TokenClass(unittest.TestCase):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json;charset=UTF-8',
                        'User-Agent': '*****',
                        'Accept-Version': '**'}
        self.url = 'https://pbsapi.aikenong.com.cn/boss/'

    def getToken(self):
        data = {"username": '13611112222', "password": 'akn2019666'}

        self.r = requests.post(self.url + 'login/', json=data, headers=self.headers)
        return {'token': self.r.json()['data']['token'], 'cookies': self.r.cookies.get_dict()}

    def test_getInfo(self):
        self.getToken()
        self.r = requests.get(self.url + '/locations/company/', json=self.getToken(), headers=self.headers)
        # print( self.r.json())

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TokenClass)
