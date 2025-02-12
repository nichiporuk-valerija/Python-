from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
firefox_options = Options()
driver = webdriver.Firefox
drivers = webdriver.Firefox

sleep(3)
driver.get("http://the-internet.herokuapp.com/entry_ad")
close_button = driver.find_element(By.XPATH, "//div[@id='modal']")
driver.execute_script("arguments[0].scrollIntoView();", close_button)
close_button.click()

sleep(3)