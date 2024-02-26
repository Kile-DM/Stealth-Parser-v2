# Данные аккаунта для selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time

with open ('resources/parser_acc.txt', 'r') as parser_acc:
    user_name, user_password = parser_acc.readlines()[0].split(':')
    parser_acc.close()
    

    group_link = 'https://ok.ru/group/70000002501616/members'

    # Добавляем опции 
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-samdbox")
    chrome_options.add_argument("start-maximized") # Открываем браузер на весь экран
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options)

    # Добавляем параметры к stealth
    stealth(
        driver,
        languages=['ru-Ru', 'ru'],
        vendor='Google Inc.',
        platform='Win32',
        webgl_vendor='Intel Inc.',
        renderer='Intel Iris OpenGL Engine',
        fix_hairline=True
    )

    # Авторизация на сайте
    url = 'https://ok.ru' # Вставляем адрес страницы в переменную
    driver.get(url) # Открываем страницу в браузере
    driver.implicitly_wait(2) # Ждём загрузки страницы
    pointer = driver.find_element(By.ID, 'field_email') # Находим поле с вводом имейла
    pointer.send_keys(user_name) # Вводим имейл
    pointer = driver.find_element(By.ID, 'field_password') # Находим поле с вводом пароля
    pointer.send_keys(user_password) # Вводим пароль
    pointer.send_keys(Keys.ENTER) # Нажимаем ENTER
    driver.implicitly_wait(2)
    

    