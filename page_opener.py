# Импортируем selenium, selenium-stealth, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import time
import random


def main():
    accs_counter = 0 # Счётчик для аккаунтов
    page_counter = 0 # Счётчик для посещенных страниц

    

    print('Начинаю работу!')
    
    with open('user_links.txt', 'r+') as file:
            links = file.read()
            links = links.split('\n')
            file.close()
    
    # Основной цикл программы
    for link in links:
        
        # Добавляем опции 
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--no-samdbox")
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
        page_opener_accs_list = ['79911608897:J8IgXZQzIy',
                                 '79310117659:8i5Fa1Y9PX',
                                 '79581035541:QTv1m0rXGg',
                                 '79918276232:4bfdWIn5bE',
                                 '79310111095:8YcBhXFXR7']
        
        user_name, user_password = page_opener_accs_list[accs_counter].split(':')   
        url = 'https://ok.ru' # Вставляем адрес страницы в переменную
        driver.get(url) # Открываем страницу в браузере
        driver.implicitly_wait(2) # Ждём загрузки страницы
        pointer = driver.find_element(By.ID, 'field_email') # Находим поле с вводом имейла
        pointer.send_keys(user_name) # Вводим имейл
        pointer = driver.find_element(By.ID, 'field_password') # Находим поле с вводом пароля
        pointer.send_keys(user_password) # Вводим пароль
        pointer.send_keys(Keys.ENTER) # Нажимаем ENTER
        driver.implicitly_wait(2) # Ждём загрузки страницы
        
        # Читаем файл и посещаем ссылки
        
        final_link = f'https://ok.ru{link}'
        driver.get(final_link)
        print(f'{final_link} страница посещена')
        sleep_time = random.randint(120, 2400)
        print(f'Ожидание для посещения следующей страницы {sleep_time / 60} минут...')
        time.sleep(sleep_time)
        page_counter += 1
        if page_counter >= random.randint(10, 31):
            accs_counter += 1
            print('Смена аккаунта')
            driver.close()
            driver.quit()
        elif accs_counter  + 1 >= len(page_opener_accs_list):
            accs_counter = 0
            print('Все аккаунты отработали')
            print(f'Ожидания следующего цикла...')
            driver.close()
            driver.quit()

    print('Завершено!')
     
if __name__ == '__main__':
    main()