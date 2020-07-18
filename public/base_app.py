#coding=utf-8
#!usr/bin/python
from appium import webdriver
from time import sleep
import os

def get_phone_size(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


def app_driver():
    capabilities = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:62001",
        "appPackage": "com.ttook.akn",
        "appActivity": "com.ttook.akn.ui.activity.common.splash.SplashActivity"
    }

    os.system("adb connect 127.0.0.1:62001")
    driver = webdriver.Remote("127.0.0.1:4723/wd/hub", capabilities)
    return driver


def swipe_left(driver, duration=300):
    width, height = get_phone_size(driver)
    start_x, start_y = 3 / 4 * width, 1 / 2 * height
    end_x, end_y = 1 / 4 * width, 1 / 2 * height
    driver.swipe(start_x, start_y, end_x, end_y, duration)


def swipe_up(driver,x1,x2,y1,y2, duration=300):
    width, height = get_phone_size(driver)
    start_x,start_y = x1 * width, y1 * height
    end_x, end_y = x2 * width, y2 * height
    driver.swipe(start_x, start_y, end_x, end_y, duration)


def login(driver):
    # driver = app_driver()
    sleep(3)
    swipe_left(driver)
    sleep(3)
    swipe_left(driver)
    sleep(3)
    swipe_left(driver)
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
