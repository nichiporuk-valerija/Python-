from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
sleep(3)
driver= webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
btn = driver.find_element(By.CSS_SELECTOR,  ".btn-primary").click()
sleep(3)
driver.quit()
