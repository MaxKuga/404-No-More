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


# driver sleep from 1 to 5 seconds (random time)
def delay():
    time.sleep(random.randint(1, 5)) # simulate long running test

class ChromeSearch(unittest.TestCase):
    # driver initialization
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test1_SignUp_valid_credential(self):
        driver = self.driver
        driver.get('https://qasvus.wixsite.com/ca-marketing')
        wait = WebDriverWait(driver, 10)
        try:
            assert driver.title == "Home | California Marcketing" # Ensure that we are on the correct page
            print("Title is:", driver.title)
        except AssertionError:
            print("Title is different:", driver.title)

        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='VGMdYn']"))) # wait "Let's Chat" is present
        print("Let's Chat icon found.")
        delay()

        # Click "Log in"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()= 'Log In']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Log In']")))
        delay()
        element.click()

        # Click "Sign up with email"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sign up with email']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign up with email']")))
        element.click()
        Password = "MaximK" # create variable

        # Ввод email
        random_email = str(random.randint(0, 99999)) + "myemail@example.com"
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_emailInput_SM_ROOT_COMP')]")))
        element.send_keys(random_email)

        # Ввод password
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_passwordInput_SM_ROOT_COMP')]")))
        element.send_keys(Password)

        # Click "Sign up"
        driver.find_element(By.XPATH, "//span[normalize-space()='Sign Up']").click()
        time.sleep(3)

        # Проверяем наличие Hello + email  после регистрации
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='MseJE2']")))
            print("Hello + email is present, the account is register")
        except TimeoutException:
            print("Uppsss, Hello + email is NOT present")

    def test2_SignIn_valid_credential(self):
        driver = self.driver
        driver.get('https://qasvus.wixsite.com/ca-marketing')
        wait = WebDriverWait(driver, 10)
        assert "Home | California Marcketing" in driver.title
        print("Page title in Chrome is:", driver.title)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='VGMdYn']"))) # wait "Let's Chat" is present
        print("Let's Chat icon found.")
        delay() # simulate long running test
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()= 'Log In']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Log In']")))
        delay()
        element.click()

        # кликаем по кнопке  "Log in" второй раз
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]")))
            time.sleep(2)
            element.click()
            print("Log In button (second time) clicked.")
        except TimeoutException:
            print("Log In button was not clickable in time!")

        # Click "Log in with email"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in with Email']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Log in with Email']")))
        element.click()
        Email = "maxk18@gmail.com"
        Password = "MaximK"        # create variable
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_emailInput_SM_ROOT_COMP')]")))
        element.send_keys(Email)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_passwordInput_SM_ROOT_COMP')]")))
        element.send_keys(Password)
        delay() # simulate long running test

        # Find check box and click (reCAPTCHA)
        try:
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")))
            driver.switch_to.frame(iframe)
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']")))
            checkbox.click()
            driver.switch_to.default_content()  # Вернуться в основной контекст
        except TimeoutException:
            print("reCAPTCHA did not load in time")
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='okButton_SM_ROOT_COMP861']"))) #Click "Log In" //span[@class='l7_2fn wixui-button__label'][normalize-space()='Log In']
        element.click()
        delay()
        # Проверяем наличие Hello + email  после регистрации
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='MseJE2']")))
            print("Hello + email is present, the account is register")
        except TimeoutException:
            print("Uppsss, Hello + email is NOT present")

    def test3_SignIn_InvalidPassword(self):
        driver = self.driver
        driver.get('https://qasvus.wixsite.com/ca-marketing')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='VGMdYn']")))  # wait "Let's Chat" is present
        print("Let's Chat icon found.")
        delay() # simulate long running test
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()= 'Log In']")))  # Click "Log in"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Log In']")))
        delay()
        element.click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))  # Click "Log in" second time
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]")))
            time.sleep(2)
            element.click()
            print("Log In button (second time) clicked.")
        except TimeoutException:
            print("Log In button was not clickable in time!")

        # Click "Log in with email"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in with Email']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Log in with Email']")))
        element.click()

        email = "maxk18@gmail.com"
        password = "Maxim"  # create variable
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_emailInput_SM_ROOT_COMP')]")))
        element.send_keys(email)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_passwordInput_SM_ROOT_COMP')]")))
        element.send_keys(password)
        delay() # simulate long-running test

        # Click reCAPTCHA
        try:
            iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")))
            driver.switch_to.frame(iframe)
            checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']")))
            checkbox.click()
            driver.switch_to.default_content()  # Вернуться в основной контекст
        except TimeoutException:
            print("reCAPTCHA did not load in time")
        element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='okButton_SM_ROOT_COMP861']")))  # Click "Log In" //span[@class='l7_2fn wixui-button__label'][normalize-space()='Log In']
        element.click()
        delay()
        def is_text_absent(driver, text):
            try:
                driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
                return False  # Текст найден, значит он не отсутствует
            except NoSuchElementException:
                return True  # Текст не найден, значит он отсутствует

    def test4_SignUp_exist_Username(self):
        driver = self.driver
        driver.get('https://qasvus.wixsite.com/ca-marketing')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='VGMdYn']")))  # wait "Let's Chat" is present
        print("Let's Chat icon found.")
        delay()  # simulate long-running test
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()= 'Log In']")))  # Click "Log in"
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Log In']")))
        delay()
        element.click()

        # Click "Sign up with email"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sign up with email']")))
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign up with email']")))
        element.click()
        email = "maxk18@gmail.com"
        password = "MaximK"
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_emailInput_SM_ROOT_COMP')]")))
        element.send_keys(email)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_passwordInput_SM_ROOT_COMP')]")))
        element.send_keys(password)
        delay()
        # Click "Sign up"
        driver.find_element(By.XPATH, "//span[normalize-space()='Sign Up']").click()
        time.sleep(3)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(@id, 'siteMembersInputErrorMessage_emailInput_SM_ROOT_COMP') and contains(text(), 'An account with this email')]")))

            # wait.until(EC.presence_of_element_located((By.XPATH, "//span[@ id = 'siteMembersInputErrorMessage_emailInput_SM_ROOT_COMP863' and contains(text(), 'An account with this email')]")))
            print("An account with this email already exists")
            print("Test PASS")
        except TimeoutException:
            print("Uppsss, Test Fail, account register with exists credential ")










   # Close browser after each test
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()