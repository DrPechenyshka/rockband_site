from flask import Flask, render_template_string
from bs4 import BeautifulSoup
import requests

app_v1 = Flask(__name__)

@app_v1.route('/')
def index():
    # Kод парсера
    url = 'https://en.m.wikipedia.org/wiki/Labyrinth_(band)'
    response = requests.get(url)
    history_text = ''
    discography_text = ''
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        history_header = soup.find('span', id='History')
        discography_header = soup.find('span', id='Discography')
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
    else:
        history_text = '<p>Ошибка при запросе страницы.</p>'
        discography_text = '<p>Ошибка при запросе страницы.</p>'

    # HTML шаблон с кнопками и контентом
    html_template = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>Информация о Labyrinth</title>
    <!-- Стили и скрипты -->
    </head>
    <body>
    <!-- Кнопки -->
    <button class="button" onclick="window.location.href='https://www.labrinth.com';">Перейти на Labrinth</button>
    <button class="button" onclick="window.location.href='https://github.com/DrPechenyshka';">Перейти на GitHub</button>
    <!-- Контент, полученный из парсера -->
    {{ history_content | safe }}
    {{ discography_content | safe }}
    <!-- JavaScript для анимации кнопок -->
    <script>
      var buttons = document.querySelectorAll(".button");

      buttons.forEach(function (button) {
        button.addEventListener("mouseover", function () {
          button.style.backgroundColor = "#555";
        });

        button.addEventListener("mouseout", function () {
          button.style.backgroundColor = "#4CAF50";
        });

        button.addEventListener("mousedown", function () {
          button.style.backgroundColor = "#333";
          button.style.boxShadow = "0 5px #666";
        });

        button.addEventListener("mouseup", function () {
          button.style.backgroundColor = "#4CAF50";
          button.style.boxShadow = "0 9px #999";
        });
      });
    </script>
    </body>
    </html>
    '''
    return render_template_string(html_template, history_content=history_text, discography_content=discography_text)

if __name__ == '__main__':
    app_v1.run(debug=True)
