import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import zipfile
import sys
import ctypes
import getpass

ctypes.windll.shcore.SetProcessDpiAwareness(True)

window = tk.Tk()
window.title("XPI Extract")
style = ttk.Style()
window.geometry("500x300")
style.configure('TLabel', font=('Arial', 12), padding=10)
style.configure('TEntry', font=('Arial', 12), padding=10)
style.configure('TButton', font=('Arial', 12), padding=10, top=10)

filename_entry_var = tk.StringVar()  # Variable für den Entry-Inhalt
filename_entry_var.set(sys.argv[1].replace(".xpi", ""))  # Setzen des Entry-Inhalts

path_label = ttk.Label(window, text="Give the path to where it should be extracted to:")
path_label.grid(row=1, column=3)

path_entry = ttk.Entry(window, textvariable=filename_entry_var, width=50)
path_entry.grid(row=2, column=3)

button = ttk.Button(window, text="Extract", command=lambda: extract_xpi(sys.argv[1]))
button.place(x=350, y=248)

def extract_xpi(filename):
    try:
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(f"{filename_entry_var.get()}")
        window.destroy()
    except:
        window.destroy()
        messagebox.showinfo("XPI Extract", "Corrupted .xpi File")

current_user = getpass.getuser()
icon_path = f"C:\\Users\\{current_user}\\VisualElements_70.ico"

window.iconbitmap(icon_path)

window.mainloop()