#coding=utf-8
#!usr/bin/python
from appium import webdriver
from time import sleep
from public import base_app
import os
driver = base_app.app_driver()
base_app.login(driver)
sleep(3)
driver.find_element_by_id("com.ttook.akn:id/iv_home_option_pest_scan").click()

sleep(3)
base_app.swipe_up(driver,0.5,0.5,0.6,0.4)
log_list = driver.find_elements_by_id("com.ttook.akn:id/iv_item_brand_com_pest_logo")
text_list = driver.find_elements_by_id("com.ttook.akn:id/tv_item_brand_com_pest_name")
a = len(text_list)
b = len(log_list)
print(u"本页条数A：%d" % a)
print(u"本页条数B：%d" % b)
for i in range(a):
    text = text_list[i].text
    n=i+1
    print("%d"%n + ":" + text)
    log_list[i].click()
    sleep(8)
    driver.back()
    sleep(3)
    # list = driver.find_elements_by_class_name("android.widget.ImageView")
    text_list = driver.find_elements_by_id("com.ttook.akn:id/tv_item_brand_com_pest_name")
sleep(3)
base_app.swipe_up(driver,0.5,0.5,0.6,0.4)
log_list1 = driver.find_elements_by_id("com.ttook.akn:id/iv_item_brand_com_pest_logo")
text_list1 = driver.find_elements_by_id("com.ttook.akn:id/tv_item_brand_com_pest_name")
a1 = len(text_list1)
b1 = len(log_list1)
print(u"本页条数A：%d" % a1)
print(u"本页条数B：%d" % b1)
for i in range(b1):
    text1 = text_list1[i].text
    n=i+1
    print("%d"%n + ":" + text1)
    log_list1[i].click()
    sleep(8)
    driver.back()
    sleep(3)
    # list = driver.find_elements_by_class_name("android.widget.ImageView")
    text_list1 = driver.find_elements_by_id("com.ttook.akn:id/tv_item_brand_com_pest_name")