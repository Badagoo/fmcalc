import tkinter as tk
import math
def click(event, screen):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

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

    i = 0
    for button in buttons:
        btn = tk.Button(frame, text=button, font="Segoe 20")
        btn.grid(row=math.floor(i / 4), column=i % 4)
        btn.bind("<Button-1>", lambda e, screen=screen: click(e, screen))
        i += 1
        
    
    CalculateWindow.protocol("WM_DELETE_WINDOW", lambda: [CalculateWindow.destroy(), root.deiconify()])