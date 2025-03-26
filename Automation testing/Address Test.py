from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from faker import Faker
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
fake = Faker()
import Helpers as H

# import from Helpers def delay(1 to 5)
H.delay1_5()


class ChromeSearch(unittest.TestCase):
    # driver initialization
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test1_Add_new_Address(self):
        driver = self.driver
        driver.get('https://qasvus.wixsite.com/ca-marketing')
        wait = WebDriverWait(driver, 10)
