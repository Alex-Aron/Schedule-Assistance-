from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv


load_dotenv()
service = Service(executable_path="chromedriver.exe")
login = webdriver.Chrome(service=service)
user_name = os.getenv("USER-NAME")
user_pass =  os.getenv("PASSWORD")
print(user_name)
print(user_pass)
login.get("https://login.ufl.edu")
username = login.find_element(By.NAME, "j_username")
username.send_keys(user_name)
password = login.find_element(By.NAME, "j_password")
password.send_keys(user_pass)
button = login.find_element(By.NAME, "_eventId_proceed")
button.click()
yesDevice = WebDriverWait(login, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="trust-browser-button"]'))
)
yesDevice.click()
time.sleep(4)
login.get("https://one.uf.edu/myschedule/2241")
time.sleep(6)
xpath_expression = '//*[@id="main-content"]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]//div[*]/div/div/div/div[2]/div/div[1]/div[2]/div/p'
name_elements = login.find_elements(By.XPATH, xpath_expression)

for name_element in name_elements:
    print(name_element.text)
time.sleep(120)
