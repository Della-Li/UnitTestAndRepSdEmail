from selenium import webdriver
from time import sleep, ctime
import webbrowser
import sys
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common import touch_actions
from module import Mail



first_url = 'http://www.baidu.com'
second_url = 'http://www.google.com'
third_url = 'http://www.126.com'
fourth_url = 'http://videojs.com'
fifth_url = 'https://www.helloweba.net/demo/2017/unlock/'
sixth_url = 'http://www.jq22.com/yanshi4976'
seventh_url = 'http://www.126.com'

driver = webdriver.Chrome()

driver.get(seventh_url)

mail = Mail(driver)
mail.login(username,password)

sleep(5)

mail.logout()

driver.quit()

