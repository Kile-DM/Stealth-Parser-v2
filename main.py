# Импортируем selenium, selenium-stealth, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import time

# Запускаем таймер
start = time.monotonic()



# Импортируем init 
from init import driver

USER_NAME = '+79969680985' # Логин аккаунта
USER_PASSWORD = '54dk7PElEg' # Пароль аккаунта

links = [] # Создаём переменную для хранения всех ссылок на страницы пользователей. Значение переменной сбрасывается при каждой итерации цикла
scrolling_counter = 0 # Добавляем счетчик скроллиннга



# Логика скрипта
print('Программа начала работу!')


    


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

# Действия после входа
url = 'https://ok.ru/znaktv/members' # Указываем страницу участников группы
driver.get(url) # Загружаем страницу участников группы
driver.implicitly_wait(2) # Ожидаем загрузки страницы    

# Основной цикл парсинга 
print('Выполнение...')
while True:  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # Скроллим страницу вниз
    try:
        driver.find_element(By.CLASS_NAME, 'link-show-more').click()# Кликаем по кнопке "Показать еще"
    except:
        scrolling_counter += 1
        print(f'Обновляю страницу {scrolling_counter}-й раз')
            # Парсинг элементов        
        posts = driver.find_elements(By.CLASS_NAME, 'user-grid-card_avatar') # Парсим все элементы блока
            
        for post in posts:
            link = post.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(link) # Добавляем ссылку в список
            
            
        if len(links) > 0:
            with open('links.txt', 'a') as f: # Открываем файл с сохраненными ссылками
                for item in links:
                    f.write(links.pop(-1) + '\n')
                    print(f'+ Сохранена ссылка: {item}')
                print(f'Всего ссылок сохранено: {len(links)}')
                result = time.monotonic() - start
                print("Program time: {:>.3f}".format(result) + " seconds.")
            
            #Записываем файл
            with open('links.txt', 'r') as f:
                s = f.read()
                s = s.split('\n')
                if s[-2] == links[-1]:
                    break
                else:
                    continue
                
                       
        # Завершение работы    
print(f'Программа завершила свою работу') # Выходим программы 
print(f'Всего ссылок сохранено: {len(links)}')
result = time.monotonic() - start
print("Program time: {:>.3f}".format(result) + " seconds.")
driver.close() # Закрываем окно
driver.quit() # Выходим из браузер





