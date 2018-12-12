# python的测试模块
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.Chrome()