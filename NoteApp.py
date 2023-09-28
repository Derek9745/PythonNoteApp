import tkinter as tk
from tkinter import *
import sqlite3

window = tk.Tk()
window.geometry("1000x600")
window.title("Note Taking App")
note_entry = tk.Text(window)
note_entry.pack()
window.config(bg="gainsboro")

def save_note():
    note = note_entry.get("1.0", tk.END)
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
    conn.commit()
    conn.close()

def view_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()

    view_window = tk.Toplevel(window)
    view_window.title("View Notes")
    view_text = tk.Text(view_window)
    for note in notes:
        view_text.insert(tk.END, note[1] + "\n")
    view_text.pack()

def clear_note():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes")
    conn.commit()
    conn.close()

view_button = tk.Button(window, text="View Notes", command=view_notes)
view_button.pack()

save_button = tk.Button(window, text="Save Note", command=save_note)
save_button.pack()

clear_button = tk.Button(window, text="Clear Note", command = clear_note)
clear_button.pack()


window.mainloop()