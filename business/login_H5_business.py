from handle.login_H5_handle import login_H5_handle
from time import sleep
class login_H5_business(object):
    def __init__(self,driver):
        self.loginh5_h = login_H5_handle(driver)
    #执行操作
    def login_email(self,username,password):
        self.loginh5_h.click_login()
        print("email:" + username)
        print("password:" + password)
        sleep(5)
        self.loginh5_h.send_useremail(username)
        sleep(5)
        self.loginh5_h.send_useremailpassword(password)
        sleep(5)
        self.loginh5_h.click_loginbtnemail()
        sleep(5)
        print("登录成功")
    #执行操作
    def login_mobile(self,username,password):
        self.loginh5_h.click_login()
        print("email:" + username)
        print("password:" + password)
        sleep(5)
        self.loginh5_h.click_mobile()
        sleep(5)
        self.loginh5_h.send_usermobile(username)
        sleep(5)
        self.loginh5_h.send_usermobilepassword(password)
        sleep(5)
        self.loginh5_h.click_loginbtnmobile()
        sleep(5)
        print("登录成功")