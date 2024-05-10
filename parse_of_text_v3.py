import webbrowser
from bs4 import BeautifulSoup
import requests

# Функция для сохранения результатов парсинга в HTML-файл
def save_html(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Функция для открытия HTML-файла в браузере
def open_html(filename):
    webbrowser.open_new_tab(filename)

# URL страницы для парсинга
url = 'https://en.m.wikipedia.org/wiki/Labyrinth_(band)'

# Отправляем HTTP-запрос и получаем ответ
response = requests.get(url)

# Проверяем, успешно ли был выполнен запрос
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим разделы History и Discography по заголовкам
    history_header = soup.find('span', id='History')
    discography_header = soup.find('span', id='Discography')

    # Извлекаем текст из разделов
    history_text = ''
    discography_text = ''
    
    if history_header:
        for elem in history_header.parent.find_next_siblings():
            if elem.name == 'h2':
                break
            history_text += str(elem)
    
    if discography_header:
        for elem in discography_header.parent.find_next_siblings():
            if elem.name == 'h2':
                break
            discography_text += str(elem)
    
    # Сохраняем результаты в HTML
    full_html_content = '<html><body>' + history_text + discography_text + '</body></html>'
    filename = 'parsed_page.html'
    save_html(full_html_content, filename)
    
    # Открываем сохраненный HTML-файл в браузере
    open_html(filename)
else:
    print(f'Ошибка при запросе страницы: статус код {response.status_code}')
