from turtle import title

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


class ChromeSearch(unittest.TestCase):
    # driver initialization
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test1_add_new_address(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        driver.get(H.g_url)
        H.delay1_5()
        H.assert_page_title(driver, title)
        H.logIn(driver)
        H.delay1_3()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ddm)))
            element = wait.until(EC.element_to_be_clickable((By.XPATH, H.ddm)))
            time.sleep(2)
            element.click()
            print("DDM found")
        except:
            print("DDM NOT FOUND")
        time.sleep(2)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.my_addresses)))
            element = wait.until(EC.element_to_be_clickable((By.XPATH, H.my_addresses)))
            time.sleep(2)
            element.click()
            print("My Addresses found")
        except:
            print("Addresses NOT FOUND")
        time.sleep(5)
        try:
            # Ждем появления элемента на странице
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='My Addresses']")))
            print("Successfully navigated to the correct page, 'root' element found.")
        except TimeoutException:
            raise Exception("Failed to navigate to the correct page. 'root' element not found.")

    # // *[ @ id = "root"] / div / main / header / h1



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()