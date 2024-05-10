import tkinter as tk
import webbrowser

def open_labrinth():
    webbrowser.open('https://www.labrinth.com')

def open_github():
    webbrowser.open('https://github.com/DrPechenyshka')

root = tk.Tk()
root.title("Переадресация кнопок")

button1 = tk.Button(root, text="Перейти на Labrinth", command=open_labrinth)
button1.pack()

button2 = tk.Button(root, text="Перейти на GitHub", command=open_github)
button2.pack()

root.mainloop()