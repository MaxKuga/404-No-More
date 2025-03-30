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

#Create variables
g_url = "https://qasvus.wixsite.com/ca-marketing"
f_url = "https://qasvus.wixsite.com/ca-marketing"
e_url = "https://qasvus.wixsite.com/ca-marketing"
m = "https://qasvus.wixsite.com/ca-marketing/account/my-addresses"
lets_chat = "//span[@class='VGMdYn']" # wait "Let's Chat" is present
log_in = "//*[text()= 'Log In']"
sign_up = "//span[normalize-space()='Sign up with email']"
input_email = "//input[starts-with(@id, 'input_input_emailInput_SM_ROOT_COMP')]"
input_password = "//input[starts-with(@id, 'input_input_passwordInput_SM_ROOT_COMP')]"
submit_sign_up = "//span[normalize-space()='Sign Up']"
hello = "//div[@class='MseJE2']"
ddm = "//*[@id = 'comp-k00e6z1w']"   # // *[ @ id = "comp-k00e6z1w"]       //div[@class='MseJE2']
my_addresses = "//*[@id='comp-k00e6z1w']"  # //span[normalize-space()='My Addresses'] //*[@id="comp-k00e6z1w"]/div/nav[2]


def assert_page_title(driver, title):
    wait = WebDriverWait(driver, 5)
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

def logIn(driver):
    wait = WebDriverWait(driver, 5)
    # Click "Log in"
    wait.until(EC.visibility_of_element_located((By.XPATH,log_in)))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, log_in)))
    time.sleep(2)
    element.click()
    # Click "Sign up with email"
    wait.until(EC.visibility_of_element_located((By.XPATH, sign_up)))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, sign_up)))
    time.sleep(1)
    element.click()
    password = "MaximK"  # create variable
    # Ввод email
    random_email = str(random.randint(0, 99999)) + "myemail@example.com"
    element = wait.until(EC.presence_of_element_located((By.XPATH,input_email)))
    element.send_keys(random_email)
    # Ввод password
    element = wait.until(EC.presence_of_element_located((By.XPATH,input_password)))
    element.send_keys(password)
    time.sleep(2)
    # Click submit "Sign up"
    driver.find_element(By.XPATH,submit_sign_up).click()
    time.sleep(3)
    # Проверяем наличие Hello + email  после регистрации
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH,hello)))
        print("Hello + email is present, the account is register")
    except TimeoutException:
        print("Uppsss, Hello + email is NOT present")

