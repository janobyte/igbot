from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from random import randint

hashtag_list = ['travelling']
already_followed = []
new_followed = []
tag = -1
follows = 0
likes = 0
comments = 0

class instab():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('https://instagram.com/')
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()


if __name__ == '__main__':
    igbot = instab('', '')
