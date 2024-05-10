import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

# URL страницы с треками артиста на Яндекс.Музыке
url = 'https://music.yandex.ru/artist/188916/tracks'

# Отправляем GET-запрос к странице
response = requests.get(url)

# Проверяем, успешно ли был выполнен запрос
if response.status_code == 200:
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем элементы, содержащие названия треков
    # Обратите внимание, что классы и структура могут измениться, и вам нужно будет их обновить
    tracks = soup.find_all('div', class_='d-track__name')

    # Выводим названия треков
    for track in tracks:
        title = track.find('a').text
        print(title)
else:
    print('Не удалось получить данные с сайта Яндекс.Музыка')
