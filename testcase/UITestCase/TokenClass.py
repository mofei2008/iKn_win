#coding=utf-8
from appium import webdriver
from time import sleep
import os
capabilities1 = {
      "platformName": "Android",
      "deviceName": "127.0.0.1:62001",
      # "deviceName": "e8df228e",
      "appPackage": "com.haitoutech.wealth",
      "appActivity": "com.haitoutech.wealth.activity.LaunchActivity"
}

capabilities2 = {
      "platformName": "Android",
      "deviceName": "127.0.0.1:62001",
      "appPackage": "com.ttook.akn",
      "appActivity": "com.ttook.akn.ui.activity.common.splash.SplashActivity"
}
os.system("adb connect 127.0.0.1:62001")
driver = webdriver.Remote("127.0.0.1:4723/wd/hub",capabilities2)
sleep(3)
driver.find_element_by_id("com.haitoutech.wealth:id/tv_login").click()
sleep(3)
driver.find_element_by_id("com.haitoutech.wealth:id/login_number").send_keys("lidetao@163.com")
sleep(3)
driver.find_element_by_id("com.haitoutech.wealth:id/login_password").send_keys("Aa111111")
sleep(3)
driver.find_element_by_id("com.haitoutech.wealth:id/login").click()