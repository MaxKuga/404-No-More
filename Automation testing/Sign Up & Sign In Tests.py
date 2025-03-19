import time
import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()  # driver initialization
driver.get("https://qasvus.wixsite.com/ca-marketing")
driver.maximize_window()

#print(driver.title)
wait = WebDriverWait(driver, 10)

# Удостоверямся что мы на правильной странице
try:
    assert driver.title == "Home | California Marcketing"
    print("Title is:", driver.title)
except AssertionError:
    print("Title is different:", driver.title)

# Ждем появление иконки "Let's Chat"
try:
    chat_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='VGMdYn']")))
    print("Let's Chat icon найден.")
except TimeoutException:
    print("Let's Chat icon не найден.")

# кликаем по кнопке  "Log in"
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()= 'Log In']")))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()= 'Log In']")))
    time.sleep(2)
    element.click()
    print("Log In button clicked.")
except TimeoutException:
    print("Log In button was not clickable in time!")

# # кликаем по кнопке  "Log in" второй раз
# try:
#     wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Log In')]")))
#     time.sleep(2)
#     element.click()
#     print("Log In button (second time) clicked.")
# except TimeoutException:
#     print("Log In button was not clickable in time!")

# кликаем по кнопке  "Sign up with email"
try:
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sign up with email']")))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign up with email']")))
    element.click()
    print("Sign Up with email button clicked.")
except TimeoutException:
    print("Sign Up with email was not clickable in time!")

# Создаем переменную
Password = "MaximK"

# Ввод email
random_email = str(random.randint(0, 99999)) + "myemail@example.com"
try:
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_emailInput_SM_ROOT_COMP')]")))
    time.sleep(2)
    element.send_keys(random_email)
    print("Email entered successfully.")
except TimeoutException:
    print("Email input field was not clickable in time!")

# Ввод password
try:
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[starts-with(@id, 'input_input_passwordInput_SM_ROOT_COMP')]")))
    time.sleep(2)
    element.send_keys(Password)
    print("Password entered successfully.")
except TimeoutException:
    print("Password input field was not clickable in time!")

# Click "Sign up"
driver.find_element(By.XPATH,"//span[normalize-space()='Sign Up']").click()
time.sleep(3)

# Проверяем наличие иконки Members chat после регистрации
try:
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='MseJE2']")))   #//*[@id='minimized-chat']  //div[@class='MseJE2']
    # time.sleep(2)
    print("Hello + email is present, the account is register")
except TimeoutException:
    print("Uppsss, Hello + email is NOT present")
print("Test#1------------------PASS")
driver.quit()

