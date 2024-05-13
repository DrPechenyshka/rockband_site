from flask import Flask, render_template_string

app_by_import = Flask(__name__)

@app_by_import.route('/')
def index():
    # Чтение текста из файла
    try:
        with open('C:\\rocksite\\content_items\\content.txt', 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        content = '<p>Файл не найден.</p>'

    # HTML шаблон с контентом из файла
    html_template = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>Текст из файла</title>
    <!-- Стили и скрипты -->
    </head>
    <body>
    <!-- Контент из файла -->
    {{ file_content | safe }}
    </body>
    </html>
    '''
    return render_template_string(html_template, file_content=content)

if __name__ == '__main__':
    app_by_import.run(debug=True)
