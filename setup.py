from tkinter import Menu
from PIL import Image, ImageTk
from functions import new_file, save_file, save_file_as, open_file, exit_out

def setup(root, text):
    menubar = Menu(root)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="New File", command=new_file, accelerator="Ctrl+N")
    fileMenu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
    fileMenu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
    fileMenu.add_command(label="Save As...", command=save_file_as, accelerator="Ctrl+Shift+S")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exit_out, accelerator="Ctrl+Q")
    menubar.add_cascade(label="Program", menu=fileMenu)
    root.config(menu=menubar)

    root.bind_all("<Control-n>", lambda e: new_file(text))
    root.bind_all("<Control-o>", lambda e: open_file(text))
    root.bind_all("<Control-s>", lambda e: save_file(text))
    root.bind_all("<Control-Shift-S>", lambda e: save_file_as(text))
    root.bind_all("<Control-q>", lambda e: exit_out())

    icon = Image.open('./assets/coplandOSLogo.png')
    photo = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(False, photo)