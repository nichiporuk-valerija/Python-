import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))


def test_form_submission():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполнение полей 
# first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
# last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
# address = driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
# email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
# phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
# zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("") 
# city = driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
# country = driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
# job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "zip-code").send_keys("")  # Оставляем пустым
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")




# Нажать кнопку 
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()



 # Проверка красного поля
alert_danger_color = "rgba(248, 215, 218, 1)"
css_value = driver.find_element(By.NAME, "zip-code").value_of_css_property(
          "background-color"     )
alert_danger_color == css_value



# Проверка остальных полец 
fields = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job", "company"
    ] 
for field_name in fields:
        field = driver.find_element(By.NAME, field_name)
        field_border_color = field.value_of_css_property("border-color")
        print(field_border_color)
        assert field_border_color == "rgb(206, 212, 218)", f"Expected green border color for {field_name}, but got {field_border_color}"