from selenium import webdriver
import time
import random
from faker import Faker


# driver sleep from 1 to 5 seconds (random time)
def delay1_5():
    time.sleep(random.randint(1, 5)) # simulate long running test

# driver sleep from 1 to 3 seconds (random time)
def delay1_3():
    time.sleep(random.randint(1, 3)) # simulate long running test

g_url = "https://qasvus.wixsite.com/ca-marketing"
f_url = "https://qasvus.wixsite.com/ca-marketing"
e_url = "https://qasvus.wixsite.com/ca-marketing"
