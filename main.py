import matplotlib
import tkinter as tk
import math
import numpy
from PIL import Image, ImageTk
import calculator

root = tk.Tk()

def CalculatorFrame():
    calculator.generate(root)

def open_frame2():
    frame2 = tk.Toplevel(root)
    frame2.title("Frame 2")
    frame2.geometry("300x300")
    frame2_label = tk.Label(frame2, text="Frame 2")
    frame2_label.pack()
def open_frame3():
    frame3 = tk.Toplevel(root)
    frame3.title("Frame 3")
    frame3.geometry("300x300")
    frame3_label = tk.Label(frame3, text="Frame 3")
    frame3_label.pack()

root.title("Main Home")
root.configure(background="grey")

calculate = Image.open('calculate.png')
calculate = ImageTk.PhotoImage(calculate)
notepad = Image.open('notepad.png')
notepad = ImageTk.PhotoImage(notepad)
functions = Image.open('functions.png')
functions = ImageTk.PhotoImage(functions)

CalculateFrameButton = tk.Button(root, image=calculate, command=CalculatorFrame, width=150, height=200)
CalculateFrameButton.grid(row=0, column=0, padx=10, pady=10)
NotepadFrameButton = tk.Button(root, image=notepad, command=open_frame2, width=150, height=200)
NotepadFrameButton.grid(row=0, column=1, padx=0, pady=10)
FunctionsFrameButton = tk.Button(root, image=functions, command=open_frame3, width=150, height=200)
FunctionsFrameButton.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()