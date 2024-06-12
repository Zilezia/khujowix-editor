from tkinter import Tk
from elements import elements

def app():
    root = Tk()
    root.title("Zextor")

    root.minsize(width=300, height=300)
    root.geometry('1000x600')
    # root.resizable(True,True)

    elements(root)

    root.mainloop()

if __name__ == "__main__":
    app()