#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


# pip install selenium
from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://www.youtube.com/watch?v=i-AXImNxCAE")
print(f'Title: "{driver.title}"')
