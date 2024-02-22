# Импортируем selenium, selenium-stealth, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth


# Данные аккаунта для selenium
user_name = '+79310117613'
user_password = '4PeGbH28Uo'

def page_saver():
    
    print('Начинаю работу!')
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
    driver.implicitly_wait(2) # Ждём загрузки страницы

    # Действия после входа
    url = 'https://ok.ru/znaktv/members' # Указываем страницу участников группы
    driver.get(url) # Загружаем страницу участников группы
    driver.implicitly_wait(2) # Ожидаем загрузки страницы    


    # Цикл прокрутки страницы
    print(f'Выполняю прокрутку страницы {url} ...')
    scroll_counter = 0
    while scroll_counter < 50:
        try:
            driver.find_element(By.CLASS_NAME, 'link-show-more').click()# Кликаем по кнопке "Показать еще"
            scroll_counter = 0
        except:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # Скроллим страницу вниз
            scroll_counter += 1
            continue  

       
    # Закрываем драйвер после завершения прокрутки и сохранения страницы
    with open(f'saved_page.txt', 'w') as f:
        f.write(driver.page_source)
        f.close()
    print(f'Страница {url} успешно сохранена!')
    driver.close()
    driver.quit()