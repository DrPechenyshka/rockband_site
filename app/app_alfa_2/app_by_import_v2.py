from flask import Flask, render_template_string

app_by_import_v2 = Flask(__name__)

@app_by_import_v2.route('/')
def index():
    # Инициализация переменных для содержимого файлов
    contents = []
    # Директория местоположения файлов с текстовой информацией пишется от их места расположения, пример: 'C:\\user\\folder\\file.txt'
    file_paths = ['content_items\\1.txt', 'content_items\\2.txt', 'content_items\\3.txt']
    
    # Чтение текста из каждого файла
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                contents.append(file.read())
        except FileNotFoundError:
            contents.append(f'<p>Файл по пути {file_path} не найден.</p>')

    # HTML шаблон с контентом из файлов
    html_template = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>Текст из файлов</title>
    <!-- Стили и скрипты -->
    </head>
    <body>
    <!-- Контент из файлов -->
    {% for content in file_contents %}
        <div>{{ content | safe }}</div>
    {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html_template, file_contents=contents)

if __name__ == '__main__':
    app_by_import_v2.run(debug=True)
