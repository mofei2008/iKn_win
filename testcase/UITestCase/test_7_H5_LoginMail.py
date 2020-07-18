from selenium import webdriver
import unittest
from time import sleep
from base.findelement import FindElement

#reload(sys)
#sys.setdefaultencoding('utf8')

Login = 'HaitouLogin'

# @ddt
class Login_H5_Mail(unittest.TestCase):
    # H5邮箱登录
    def setUp(self):
        print('开始执行测试用例：')
        self.driver = webdriver.Chrome()  # 选择谷歌浏览器
        # 打开url
        url = 'https://h5advisor.haitoutech.com/'
        self.driver.get(url)  # 打开百度页面
        self.driver.maximize_window()

    def test_1(self):
        sleep(2)
        FindElement.configsplit(self,Login,'loginindex').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        # 关闭浏览器
        self.driver.close()

    def tearDown(self):
        pass
# 登录操作
#     def test_1(self):
#         '''点击货币基金'''
#         login_h5.login_mail(self.browser)
#         self.browser.find_element_by_css_selector(".footer-con li:nth-of-type(4)").click()
#         sleep(2)
#         self.browser.find_element_by_css_selector(".fund").click()
#         title1 = self.browser.title
#         print(title1)
#         self.assertEqual(u'美元货币基金', title1, msg='title不对！')
#         sleep(3)
#         self.browser.back()
#         self.browser.find_element_by_xpath("//span[1]/img").click()
#
#         sleep(3)
#         self.browser.quit()
#
#     def test_2(self):
#         '''点击私募债券'''
#         login_h5.login_mail(self.browser)
#         self.browser.find_element_by_css_selector(".footer-con li:nth-of-type(4)").click()
#         sleep(2)
#         self.browser.find_element_by_css_selector(".asstes span").click()
#         title1 = self.browser.title
#         print(title1)
#         self.assertEqual(u'美国私募债券', title1, msg='title不对！')
#         sleep(2)
#         self.browser.back()
#         sleep(2)
#         self.browser.quit()
#
#     def test_3(self):
#         '''点击卡券包'''
#         login_h5.login_mail(self.browser)
#         self.browser.find_element_by_css_selector(".footer-con li:nth-of-type(4)").click()
#         sleep(2)
#         self.browser.find_element_by_css_selector(".my-user-operate ul li:nth-of-type(1)").click()
#         title1 = self.browser.title
#         print(title1)
#         self.assertEqual(u'卡券包', title1, msg='title不对！')
#         sleep(2)
#         self.browser.back()
#         sleep(2)
#         self.browser.quit()
#
#     def test_4(self):
#         '''点击回款日历'''
#         login_h5.login_mail(self.browser)
#         self.browser.find_element_by_css_selector(".footer-con li:nth-of-type(4)").click()
#         sleep(2)
#         self.browser.find_element_by_css_selector(".my-user-operate ul li:nth-of-type(2)").click()
#         title1 = self.browser.title
#         print(title1)
#         self.assertEqual(u'回款日历', title1, msg='title不对！')
#         sleep(2)
#         self.browser.back()
#         sleep(2)
#         self.browser.quit()
#
#     def test_5(self):
#         '''点击资金明细'''
#         login_h5.login_mail(self.browser)
#         self.browser.find_element_by_css_selector(".footer-con li:nth-of-type(4)").click()
#         sleep(2)
#         self.browser.find_element_by_css_selector(".my-user-operate ul li:nth-of-type(3)").click()
#         title1 = self.browser.title
#         print(title1)
#         self.assertEqual(u'资金明细', title1, msg='title不对！')
#         sleep(2)
#         self.browser.back()
#         sleep(2)
#         self.browser.quit()
#
#     def test_6(self):
#         '''点击银行卡'''
#         login_h5.login_mail(self.browser)
#         self.browser.find_element_by_css_selector(".footer-con li:nth-of-type(4)").click()
#         sleep(2)
#         self.browser.find_element_by_css_selector(".my-user-operate ul li:nth-of-type(4)").click()
#         title1 = self.browser.title
#         print(title1)
#         self.assertEqual(u'银行卡', title1, msg='title不对！')
#         sleep(2)
#         self.browser.back()
#         sleep(2)
#         self.browser.quit()





if __name__ == "__main__":
    Login_H5_Mail()