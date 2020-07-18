#coding=utf-8
from appium import webdriver
from time import sleep
import os
from public import base
def login():
      driver = base.app_driver()
      sleep(3)
      base.swipe_left(driver)
      sleep(3)
      base.swipe_left(driver)
      sleep(3)
      base.swipe_left(driver)
      sleep(3)
      driver.find_element_by_id("com.ttook.akn:id/o_guide_enter_but").click()
      sleep(3)
      driver.find_element_by_id("com.ttook.akn:id/but_pws_login").click()
      sleep(3)
      driver.find_element_by_id("com.ttook.akn:id/et_login_pws_phoneNumber").send_keys("18610806332")
      sleep(3)
      driver.find_element_by_id("com.ttook.akn:id/et_login_pws").send_keys("Aa111111")
      sleep(3)
      driver.find_element_by_id("com.ttook.akn:id/but_login_pws").click()

if __name__ == '__main__':
    login()