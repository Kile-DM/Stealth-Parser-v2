# Импортируем selenium, selenium-stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

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
