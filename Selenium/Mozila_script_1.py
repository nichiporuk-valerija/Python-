from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
firefox_options = Options()
driver = webdriver.Firefox(options=firefox_options)


driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)
close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
driver.execute_script("arguments[0].scrollIntoView();", close_button)
close_button.click()

sleep(3)
driver.quit()



