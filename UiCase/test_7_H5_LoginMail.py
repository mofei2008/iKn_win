from selenium import webdriver
import unittest
from business.login_H5_business import login_H5_business
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
Login = 'HaitouLogin'

class Login_H5(unittest.TestCase):
    print('开始执行测试用例：')
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = 'https://h5advisor.haitoutech.com/'
        self.driver.get(url)  # 打开百度页面
        self.driver.maximize_window()
        self.loginh5 = login_H5_business(self.driver)

    def test_login_email(self):
        self.loginh5.login_email('lidetao@163.com','Aa111111')

    def test_login_mobile(self):
        self.loginh5.login_mobile('18610806332','Aa111111')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()