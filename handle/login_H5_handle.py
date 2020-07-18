from page.login_H5_page import login_H5_page
class login_H5_handle(object):
    def __init__(self,driver):
        self.loginH5_pg = login_H5_page(driver)
    def click_login(self):
        self.loginH5_pg.get_login_element().click()
    def send_useremail(self,username):
        self.loginH5_pg.get_useremail_element().send_keys(username)
    def send_usermobile(self,username):
        self.loginH5_pg.get_usermobile_element().send_keys(username)
    def send_useremailpassword(self,password):
        self.loginH5_pg.get_emailpass_element().send_keys(password)
    def send_usermobilepassword(self,password):
        self.loginH5_pg.get_mobilepass_element().send_keys(password)
    def click_loginbtnemail(self):
        self.loginH5_pg.get_btn_emailelement().click()
    def click_loginbtnmobile(self):
        self.loginH5_pg.get_btn_mobileelement().click()
    def click_mobile(self):
        self.loginH5_pg.get_mobileclick_element().click()
    def send_usercode(self):
        pass
    def get_text(self):
        pass