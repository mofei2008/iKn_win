#coding=utf-8
#!usr/bin/python
from selenium import webdriver
import unittest
from time import sleep

print('开始执行测试用例：')
driver = webdriver.Chrome()  #选择谷歌浏览器
#打开url
url = "https://boss.aikenong.com.cn/customer"
driver.get(url)  #打开首页页面
sleep(10)
driver.find_element_by_css_selector(".is-required:nth-of-type(2) .el-input__inner").send_keys("13611112222")
sleep(3)
driver.find_element_by_css_selector("div:nth-of-type(3) > .el-form-item__content > .el-input > .el-input__inner").send_keys("akn2019666")
#driver.maximize_window()
sleep(5)
driver.find_element_by_class_name("login-btn").click()
sleep(5)
driver.get("https://boss.aikenong.com.cn/land")
sleep(10)
list = driver.find_elements_by_class_name("el-card__body")
print(list)
a = len(list)
print(u"本页条数：%d" %a)

for i in range(a):
    text = list[i].text
    b=i+1
    print("%d"%b + ":" + text)
    list[i].click()
    sleep(3)
    url = driver.current_url
    print("当前页面URL：%s"%url)
    driver.back()
    sleep(5)
    list = driver.find_elements_by_class_name("el-card__body")
    # 关闭浏览器
driver.close()