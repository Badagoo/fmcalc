import tkinter as tk
import math

def generate(root):
    CalculateWindow = tk.Toplevel(root)
    CalculateWindow.title("Calculate")
    root.withdraw()

    # focus on this frame
    CalculateWindow.focus_force()

    screen = tk.StringVar()
    entry = tk.Entry(CalculateWindow, textvar=screen, font="Segoe 20")
    entry.pack(fill="x")

    frame = tk.Frame(CalculateWindow)
    frame.pack()

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    for buttonnum, button in enumerate(buttons):
        btn = tk.Button(frame, text=button, font="Segoe 20")
        btn.grid(row=math.floor(buttonnum / 4), column=buttonnum % 4)
    
    CalculateWindow.protocol("WM_DELETE_WINDOW", lambda: [CalculateWindow.destroy(), root.deiconify()])