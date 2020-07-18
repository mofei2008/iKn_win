#coding=utf-8
#!usr/bin/python
from appium import webdriver
from time import sleep
from public import base_app
import os
driver = base_app.app_driver()
base_app.login(driver)
sleep(3)
driver.find_element_by_id("com.ttook.akn:id/iv_home_option_quote").click()
sleep(3)
# print(u"本页条数a：%d" %a)
for x in range(3):
    text_list = driver.find_elements_by_id("com.ttook.akn:id/tv_news_title")
    a = len(text_list)
    print(u"本页条数a：%d" % a)
    for i in range(a):
        text = text_list[i].text
        n=i+1
        print("%d"%n + ":" + text)
        text_list[i].click()
        sleep(8)
        driver.back()
        sleep(3)
        # list = driver.find_elements_by_class_name("android.widget.ImageView")
        text_list = driver.find_elements_by_id("com.ttook.akn:id/tv_news_title")
    sleep(3)
    base_app.swipe_up(driver)
