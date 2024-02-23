# Импортируем selenium, selenium-stealth, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import time
import random


def main():
    counter = 0 # Счетчик посещения страниц
    # Данные аккаунта для selenium
    user_name = '+79310117613'
    user_password = '4PeGbH28Uo'

    print('Начинаю работу!')

    group_link = 'https://ok.ru/group/70000002413040/members'

    # Добавляем опции 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-samdbox")
    #chrome_options.add_argument("start-maximized") # Открываем браузер на весь экран
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
    driver.implicitly_wait(2) # Ждём загрузки страницы

    # Действия после входа
    url = group_link # Указываем страницу участников группы
    driver.get(url) # Загружаем страницу участников группы
    driver.implicitly_wait(2) # Ожидаем загрузки страницы  
    
    # Читаем файл и посещаем ссылки
    with open('user_links.txt', 'r+') as file:
        links = file.read()
        links = links.split('\n')
        for link in links:
            final_link = f'https://ok.ru/{link}'
            #driver.get(final_link)
            print(f'{final_link} страница посещена')
            time.sleep(random.randint(1, 60))
            counter += 1
            if counter >= 200:
                break
        file.close()
 
    print('Работа завершена!')
    driver.close() # Закрываем окно браузера
    driver.quit() # Закрываем браузер
    
    
if __name__ == '__main__':
    main()