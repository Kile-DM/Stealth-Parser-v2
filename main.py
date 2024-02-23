# Импортируем selenium, selenium-stealth, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
from bs4 import BeautifulSoup


def main():
    # Данные аккаунта для selenium
    user_name = '+79310117613'
    user_password = '4PeGbH28Uo'

    print('Начинаю работу!')

    group_link = 'https://ok.ru/group/70000002413040/members'

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
    url = group_link # Указываем страницу участников группы
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
            soup = BeautifulSoup(driver.page_source, 'html.parser') # Получаем код страницы с помощью BeautifulSoup
            user_cards = soup.find_all('div', class_='user-grid-card')
            scroll_counter += 1
            for user_card in user_cards:
                user_link = user_card.find('a').get('href')
                with open('user_links.txt', 'a+') as file:
                    file.seek(0)
                    if user_link in file.read():
                        continue
                    else:
                        file.write(f'{user_link}\n')
                        print(f'Сохранена ссылка на пользователя: {user_link}')
                        file.close()
                        file.close()

    # Закрываем браузер          
    print('Завершено!')
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
        
      