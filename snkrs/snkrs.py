import os
import pytest

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

desird_caps = {}

# 设备信息
desird_caps['platformName'] = 'Android'
desird_caps['platformVersion'] = '6.0'
desird_caps['deviceName'] = 'dc3d96c3'
# app信息
desird_caps['appPackage'] = 'com.nike.snkrs'
desird_caps['appActivity'] = '.feed.activities.TheWallActivity'

drivers = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desird_caps)

ele = drivers.find_element_by_id('item_threadgroup_single_column_card_cta')

ele.get_attribute('text')