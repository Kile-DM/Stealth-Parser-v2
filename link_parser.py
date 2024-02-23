from bs4 import BeautifulSoup

def link_parser():
        # Открываем сохраненную страницы и парсим её для получения данных о пользователях.
    with open('saved_page.txt') as page:
        soup = BeautifulSoup(page, 'html.parser')
        page.close()
        
        # Парсим и сохраняем ссылки пользователей
        user_cards = soup.find_all('div', class_='user-grid-card')
        for user_card in user_cards:
            user_link = user_card.find('a').get('href')
            with open('user_links.txt', 'a') as file:
                file.write(f'https://ok.ru/{user_link}' + '\n')
                file.close()
            
    print('Ссылки сохранены в файл user_links.txt')

