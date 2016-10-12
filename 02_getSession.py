#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://mp.weixin.qq.com')
#assert 'Yahoo' in browser.title
#print driver.title

url = driver.command_executor._url
#print url
session_id = driver.session_id
#print session_id


f = open('session.txt','w')
#print f
f.write(str(session_id))
f.close()

f2 = open('url.txt','w')
#print f2
f2.write(str(url))
f2.close()

element = driver.find_element_by_id("account")
element.send_keys("your account")
e = driver.find_element_by_id("pwd")
e.send_keys("your psw")
e = driver.find_element_by_id("loginBt")
e.click()

