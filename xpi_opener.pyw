import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import zipfile
import sys
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

def start_gui(file_path=None):
    win1 = tk.Tk()
    win1.withdraw()
    win = tk.Toplevel(win1)
    win.transient(win1)
    win.title("XPI Extract")
    win.focus_force()

    style = ttk.Style()
    style.configure('TLabel', font=('Arial', 12), padding=10)
    style.configure('TEntry', font=('Arial', 12), padding=10)
    style.configure('TButton', font=('Arial', 12), padding=10, top=10)

    filename_entry_var = tk.StringVar()
    filename_entry_var.set(file_path.replace(".xpi", "") if file_path else "")

    path_label = ttk.Label(win, text="Give the path to where it should be extracted to:")
    path_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

    path_entry = ttk.Entry(win, textvariable=filename_entry_var, width=50)
    path_entry.grid(row=1, column=0, sticky="w", padx=30)

    button = ttk.Button(win, text="Extract", command=lambda: extract_xpi(file_path))
    button.grid(row=2, column=1, padx=20, pady=10)

    def on_closing():
        win1.destroy()

    def extract_xpi(filename):
        try:
            with zipfile.ZipFile(filename, "r") as zip_ref:
                zip_ref.extractall(f"{filename_entry_var.get()}")
            win.destroy()
            win1.destroy()
        except Exception as e:
            win.destroy()
            messagebox.showinfo("XPI Extract", f"Ein Fehler ist aufgetreten: {str(e)}")
            win1.destroy()

    icon_path = r"C:\Program Files (x86)\XPI Extract\VisualElements_70.ico"
    win.iconbitmap(icon_path)
    win.resizable(False, False)  # Fenstergröße nicht änderbar machen

    win.protocol("WM_DELETE_WINDOW", on_closing)

    win.mainloop()

try:
    file_path = None
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if file_path:
            start_gui(file_path)
    else:
        if not file_path:
            win1 = tk.Tk()
            win1.withdraw()
            icon_path = r"C:\Program Files (x86)\XPI Extract\VisualElements_70.ico"
            win1.iconbitmap(icon_path)
            file_path = filedialog.askopenfilename(filetypes=[("XPI files", "*.xpi")])
            print(file_path.encode())
            win1.destroy()
            if not file_path.encode() == b'':
                start_gui(file_path)
except Exception as e:
    print(f"An error occurred: {e}")