from bs4 import BeautifulSoup
import requests

# Задаем URL страницы Wikipedia о группе Labyrinth
url = 'https://en.m.wikipedia.org/wiki/Labyrinth_(band)'

# Отправляем HTTP-запрос и получаем ответ
response = requests.get(url)

# Проверяем, успешно ли был выполнен запрос (код ответа 200)
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим элементы с текстом на странице
    # Например, можно извлечь текст из тегов <p>
    for paragraph in soup.find_all('p'):
        print(paragraph.text)
else:
    print(f'Ошибка при запросе страницы: статус код {response.status_code}')