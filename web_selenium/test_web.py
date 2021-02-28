from selenium import webdriver
import time

def test_web():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com/')
    time.sleep(8)