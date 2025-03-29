import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from faker import Faker
import random
import time
from webdriver_manager.core import driver
from selenium.webdriver.common.action_chains import ActionChains
fake = Faker()

# driver sleep from 1 to 5 seconds (random time)
def delay1_5():
    time.sleep(random.randint(1, 5)) # simulate long running test

# driver sleep from 1 to 3 seconds (random time)
def delay1_3():
    time.sleep(random.randint(1, 3)) # simulate long running test

g_url = "https://qasvus.wixsite.com/ca-marketing"
f_url = "https://qasvus.wixsite.com/ca-marketing"
e_url = "https://qasvus.wixsite.com/ca-marketing"

lets_chat = "//span[@class='VGMdYn']" # wait "Let's Chat" is present

wait = WebDriverWait(driver, 5)

def assert_page_title(driver, title):
    try:
        assert driver.title == "Home | California Marcketing"  # Ensure that we are on the correct page
        print("Title is:", driver.title)
    except AssertionError:
        print("Title is different:", driver.title)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, lets_chat)))
        print("Let's Chat icon found.")
    except TimeoutException:
        print("Let's Chat icon not found")