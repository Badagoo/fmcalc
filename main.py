import tkinter as tk
from PIL import Image, ImageTk
import calculator


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("FM CALCULATOR")
        self.configure(background="grey")

        self.buttons()

        self.mainloop()

    def buttons(self):
        calculate = Image.open('assets\\calculate.png')
        calculate = ImageTk.PhotoImage(calculate)
        notepad = Image.open('assets\\notepad.png')
        notepad = ImageTk.PhotoImage(notepad)
        functions = Image.open('assets\\functions.png')
        functions = ImageTk.PhotoImage(functions)

        MenuButton(self, calculate, lambda: calculator.generate(self), 150, 200).grid(row=0, column=0, padx=10, pady=10)
        MenuButton(self, notepad, lambda: calculator.generate(self), 150, 200).grid(row=0, column=1, padx=0, pady=10)
        MenuButton(self, functions, lambda: calculator.generate(self), 150, 200).grid(row=0, column=2, padx=10, pady=10)


class MenuButton(tk.Button):
    def __init__(self, parent, image, command, width, height):
        tk.Button.__init__(self, parent, image=image, command=command, width=width, height=height)
        self.image = image
        self.command = command
        self.width = width
        self.height = height

class ButtonImage():
    def __init__(self, image):
        self.image = Image.open(image)
        self.image = ImageTk.PhotoImage(self.image)


App()