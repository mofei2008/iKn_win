from oper.read_Element import ReadConfig

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def configsplit(self,sections,option):
        data = ReadConfig.get_config_str(sections,option)
        # print(data)
        by = data.split('>')[0]
        # print(by)
        value = data.split('>')[1]
        # print(value)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'class':
                return self.driver.find_element_by_class_name(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    configsplit('HaitouLogin', 'loginindex')