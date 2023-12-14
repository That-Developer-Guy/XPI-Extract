import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import zipfile
import sys
import ctypes
import getpass

ctypes.windll.shcore.SetProcessDpiAwareness(True)

win1 = tk.Tk()
win1.withdraw()
win = tk.Toplevel(win1)
win.transient(win1)
win.title("XPI Extract")

style = ttk.Style()
win.geometry("500x300")
style.configure('TLabel', font=('Arial', 12), padding=10)
style.configure('TEntry', font=('Arial', 12), padding=10)
style.configure('TButton', font=('Arial', 12), padding=10, top=10)
filename_entry_var = tk.StringVar()  # Variable für den Entry-Inhalt
filename_entry_var.set(sys.argv[1].replace(".xpi", ""))  # Setzen des Entry-Inhalts
path_label = ttk.Label(win, text="Give the path to where it should be extracted to:")
path_label.grid(row=1, column=3)
path_entry = ttk.Entry(win, textvariable=filename_entry_var, width=50)
path_entry.grid(row=2, column=3)
button = ttk.Button(win, text="Extract", command=lambda : extract_xpi(sys.argv[1]))
button.place(x=350, y=248)

def extract_xpi(filename):
    try:
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(f"{filename_entry_var.get()}")
        win.destroy()
        win1.destroy()
    except:
        win.destroy()
        messagebox.showinfo("XPI Extract", "An Error occured!")
        win1.destroy()

current_user = getpass.getuser()
icon_path = f"C:\\Users\\{current_user}\\VisualElements_70.ico"

win.iconbitmap(icon_path)

win.maxsize(500,300)
win.minsize(500,300)


win.mainloop()