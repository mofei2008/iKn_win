from base.findelement import FindElement
class login_H5_page(object):
    def __init__(self,driver):
        self.get_ele = FindElement(driver)
    def get_login_element(self):
        return self.get_ele.configsplit('HaitouLogin','loginindex')
    def get_useremail_element(self):
        return self.get_ele.configsplit('HaitouLogin','useremail')
    def get_usermobile_element(self):
        return self.get_ele.configsplit('HaitouLogin','usermobile')
    def get_emailpass_element(self):
        return self.get_ele.configsplit('HaitouLogin','emailpass')
    def get_mobilepass_element(self):
        return self.get_ele.configsplit('HaitouLogin','mobilepass')
    def get_btn_emailelement(self):
        return self.get_ele.configsplit('HaitouLogin','loginbtnemail')
    def get_btn_mobileelement(self):
        return self.get_ele.configsplit('HaitouLogin','loginbtnmobile')
    def get_mobileclick_element(self):
        return self.get_ele.configsplit('HaitouLogin','user_mobileclick')

if __name__ == "__main__":
    login_H5_page().get_btn_element('HaitouLogin','loginbtn')