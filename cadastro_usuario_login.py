import sqlite3
from tkinter import *


conn = sqlite3.connect('database.db')
c = conn.cursor()


c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        senha TEXT NOT NULL
    )
''')

def register_user():
    login = login_entry.get()
    senha = senha_entry.get()

    
    c.execute("SELECT * FROM users WHERE login=?", (login,))
    user = c.fetchone()

    if user:
        message_label.config(text="Login already exists!")
    else:
        
        c.execute("INSERT INTO users (login, senha) VALUES (?, ?)", (login, senha))
        conn.commit()
        message_label.config(text="Registrado com sucesso!")

        
        login_entry.delete(0, END)
        senha_entry.delete(0, END)


window = Tk()


login_label = Label(window, text="Login:")
login_label.pack()
login_entry = Entry()
login_entry.pack()


senha_label = Label(window, text="Senha:")
senha_label.pack()
senha_entry = Entry()
senha_entry.pack()


register_button = Button(window, text="Register", command=register_user)
register_button.pack()


message_label = Label(window, text="")
message_label.pack()


window.mainloop()


conn.close()