#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:03:39 2019

@author: emmanuel
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path=r'/usr/local/bin/geckodriver')
driver.get("https://unipython.com/los-mejores-ide-python-instalar-python-os-window-linux/")
assert "Python" in driver.title
elem = driver.find_element_by_name("s")
elem.clear()
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source