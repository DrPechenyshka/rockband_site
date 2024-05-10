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
    
    # Получаем HTML содержимое всей страницы (или части, которую вы хотите сохранить)
    page_html = soup.prettify()
    
    # Сохраняем HTML в файл
    filename = 'parsed_page.html'
    save_html(page_html, filename)
    
    # Открываем сохраненный HTML-файл в браузере
    open_html(filename)
else:
    print(f'Ошибка при запросе страницы: статус код {response.status_code}')
