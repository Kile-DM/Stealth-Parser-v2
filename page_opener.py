from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import random
import time

# Данные аккаунта для selenium
USER_NAME = '+79969680985' # Логин аккаунта
USER_PASSWORD = '54dk7PElEg' # Пароль аккаунта

print('Начинаю работу!')
# Добавляем опции 
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
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
pointer.send_keys(USER_NAME) # Вводим имейл
pointer = driver.find_element(By.ID, 'field_password') # Находим поле с вводом пароля
pointer.send_keys(USER_PASSWORD) # Вводим пароль
pointer.send_keys(Keys.ENTER) # Нажимаем ENTER
driver.implicitly_wait(2) # Ждём загрузки страницы




with open('user_links.txt', 'w+') as f:
    links = f.strip('\n') # Указываем страницу участников группы
    for i in range(51):
        print(f'Загружаю страницу {links[i]} ...')
        driver.get(links[i]) # Загружаем страницу 
        time.sleep(random.randrange(1, 10)) # Ждём загрузки страницы # Ожидаем загрузки страницы
        print(f'Страница {links[i]} посещена!')
        links.pop(0)
        
        
    f.write(links)    
    links.close()
        # Завершение работы программы
    print('Закрываю драйвер...')
    driver.close()
    driver.quit()
    print('Завершаю работу!')
      