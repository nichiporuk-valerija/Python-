from selenium import webdriver
from selenium.webdriver.common.by import By

# Запускаем браузер Chrome через Selenium
driver = webdriver.Chrome()

# Открываем нужную страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Находим кнопку Add Element и кликаем пять раз
add_element_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Element')]")
for _ in range(5):
    add_element_button.click()

# Собираем все кнопки Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")

# Выводим количество найденных кнопок Delete
print(f'Количество кнопок Delete: {len(delete_buttons)}')