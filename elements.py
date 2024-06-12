import os
from tkinter import *

from functions import exit_out
from setup import setup

def elements(root):
    # folder_frame = Frame(root, width=300)
    # folder_frame.pack(side='left', fill='y')
    
    # button1 = Button(folder_frame, text="Button", command=lambda: print("I've been pressed!"))
    # button1.pack(pady=5)
    # button2 = Button(folder_frame, text="Exit", command=exit_out)
    # button2.pack(pady=10)

    text = Text(root, wrap='word')
    text.pack(side='right', fill='both', expand=True)
    
    folder_frame = Frame(root, width=200, bg='gray')
    folder_frame.pack(side=LEFT, fill=BOTH)
    
    for element in os.listdir('./save-location'):
        file_frame = Frame(folder_frame, width=200, height=25, bg='#b22222')
        file_label = Label(file_frame, text=element, bg='#b22222', fg='white')
        file_label.place(anchor='nw')
        file_frame.pack()
    
    # label = Label(text, text="label.")
    # label.pack(pady=10)

    setup(root, text)