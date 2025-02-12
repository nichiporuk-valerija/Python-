from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()  
driver.get("http://the-internet.herokuapp.com/login")
username = driver.find_element(By.ID,"username")
username.send_keys('tomsmith')
sleep(2)
password = driver.find_element(By.ID,"password")
password.send_keys('SuperSecretPassword!')
sleep(2)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']") 
login_button.click()