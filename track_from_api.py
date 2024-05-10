from flask import Flask, render_template
import requests
from yandex_music import Client

app = Flask(__name__)

# Авторизация в Yandex Music API (замените 'your_token' на ваш личный токен)
client = Client('your_token')

@app.route('/')
def index():
    # Получаем список треков с помощью Yandex Music API
    tracks = client.artists(188916).tracks
    track_titles = [track['title'] for track in tracks]
    
    # Возвращаем HTML-страницу со списком треков
    return render_template('tracks.html', track_titles=track_titles)

if __name__ == '__main__':
    app.run()