import sys
import os
from tkinter import END
from tkinter.filedialog import asksaveasfile, askopenfile

base_dir = './save-location/'
fileName = "new_file.txt"

def new_file(text):
    text.delete(0.0, END)
    
def save_file(text):
    file_dest = os.path.join(base_dir, fileName)
    t = text.get(0.0, END)
    with open(file_dest, "w") as f:
        f.write(t)
    
def save_file_as(text):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    f = asksaveasfile(mode='w', defaultextension='.txt', initialdir=base_dir)
    if f is not None:
        t = text.get(0.0, END)
        f.write(t.rstrip())
        
def open_file(text):
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def exit_out():
    print("Exitting...")
    sys.exit(0)

def unique_filename(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    unique_name = filename
    
    while os.path.exists(os.path.join(directory, unique_name)):
        unique_name = f"{base}({counter}){ext}"
        counter += 1
    
    return os.path.join(directory, unique_name)