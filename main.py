import tkinter as tk
from PIL import Image, ImageTk
import calculator

TITLE = "FM CALCULATOR"
BGCHOICE = "grey"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.mainloop()

            
        #tk.Button(self, image=NotepadImage, command=lambda: calculator.generate(self), width=150, height=200).grid(row=0, column=1, padx=0, pady=10)
        #tk.Button(self, image=FunctionsImage, command=lambda: calculator.generate(self), width=150, height=200).grid(row=0, column=2, padx=10, pady=10)

class StartPage(tk.Tk):
    def __init__(self, title, bg):
        tk.Tk.__init__(self):



App(TITLE, BGCHOICE)