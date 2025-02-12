from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
sleep(3)
driver.get("http://uitestingplayground.com/classattr")
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()
sleep(3)
driver.quit()

