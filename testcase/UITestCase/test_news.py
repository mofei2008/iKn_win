#coding=utf-8
#!usr/bin/python
from appium import webdriver
from time import sleep
from public import base_app
import os

driver = base_app.app_driver()
base_app.login(driver)
sleep(3)
base_app.swipe_up(driver)
text_list = driver.find_elements_by_id("com.ttook.akn:id/tv_news_title")
b = len(text_list)
# print(u"本页条数a：%d" %a)
print(u"本页条数b：%d" %b)
for i in range(b):
    text = text_list[i].text
    n=i+1
    print("%d"%n + ":" + text)
    text_list[i].click()
    sleep(8)
    driver.back()
    sleep(3)
    # list = driver.find_elements_by_class_name("android.widget.ImageView")
    text_list = driver.find_elements_by_id("com.ttook.akn:id/tv_news_title")
