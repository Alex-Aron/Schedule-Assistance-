from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
import logging

# Set the logging level to suppress non-fatal error messages
logging.basicConfig(level=logging.ERROR)


load_dotenv()
service = Service(executable_path="chromedriver.exe")
login = webdriver.Chrome(service=service)
search = webdriver.Chrome(service=service)
user_name = os.getenv("USER-NAME")
user_pass =  os.getenv("PASSWORD")
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
cookies_done = False


for name_element in name_elements:
    search.get("https://www.ratemyprofessors.com/")
    search.implicitly_wait(20)
    if not cookies_done:
        cookies = WebDriverWait(search, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/button'))
            )
        cookies.click()
    cookies_done = True
    #search_by_professor = WebDriverWait(search, 10).until(
    #EC.presence_of_element_located((By.CLASS_NAME, 'HomepageHero__HeroToggle-rvkinu-3 eOMiLm'))
    #3)
    #search_by_professor.click()
    time.sleep(4)
    input_element = search.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[3]/div[2]')
    input_element.clear()
    input_element.send_keys(name_element.text + Keys.ENTER)
    link = WebDriverWait(search, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[3]/a/div/div[2]/div[1]'))
    )
    link.click()
    rating = search.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[1]/div[1]/div/div[1]')
    difficulty = search.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[3]/div[2]/div[1]')
    retakers = search.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]')
    print(f'{name_element.text}\'s Stats:')
    print(f'  1. Rating - {rating.text}/5')
    print(f'  2. Difficulty Level - {difficulty.text}/5')
    print(f'  3. Percentage of Retakers - {retakers.text}')
time.sleep(120)
login.quit()