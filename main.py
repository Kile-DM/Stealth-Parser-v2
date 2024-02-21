# Импортируем selenium, selenium-stealth, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth


# Данные аккаунта для selenium
USER_NAME = '+79969680985' # Логин аккаунта
USER_PASSWORD = '54dk7PElEg' # Пароль аккаунта


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

# Действия после входа
url = 'https://ok.ru/myogibenin/members' # Указываем страницу участников группы
driver.get(url) # Загружаем страницу участников группы
driver.implicitly_wait(2) # Ожидаем загрузки страницы    

# Основной цикл парсинга 
print('Выполнение...')


# Переменные
links = [] # Создаём переменную для хранения всех ссылок на страницы пользователей. Значение переменной сбрасывается при каждой итерации цикла





while True:
    scroll_counter = 0 # Счётчик скролла
    if scroll_counter < 50:
        try:
            driver.find_element(By.CLASS_NAME, 'link-show-more').click()# Кликаем по кнопке "Показать еще"
        except:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # Скроллим страницу вниз
            scroll_counter += 1 # Увеличиваем счётчик скролла
            continue  
        finally:
            print('Прокрутка страницы завершена')
            driver.close()
            driver.quit() 

    
    
        
       
        





    





