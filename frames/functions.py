import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

MAINTITLE = "Functions"
FUNC1 = "Amortisation Table"
FUNC2 = "Finance Solver"
FUNC3 = "Box Plot"
FUNC4 = "Regression"
BGCHOICE = "#353333"
WIDGETCOLOUR = "#D9D9D9"
FONT = "Segoe_UI 15"

class FunctionsController(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.title(MAINTITLE)
        self.geometry("400x210")
        self.iconbitmap("assets\FMLogo.ico")
        self.resizable(False, False)
        self.focus_force()

        self.frames = {}

        for F in (SelectScreen, AmortisationTable, FinanceSolver, BoxPlot, Regression):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SelectScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class SelectScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.configure(bg=BGCHOICE)

        Button(self, parent, FUNC1).place(x=10, y=10, width=380, height=40)
        Button(self, parent, FUNC2).place(x=10, y=60, width=380, height=40)
        Button(self, parent, FUNC3).place(x=10, y=110, width=380, height=40)
        Button(self, parent, FUNC4).place(x=10, y=160, width=380, height=40)

class AmortisationTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.configure(bg=BGCHOICE)

        label = tk.Label(self, text="GET OUT", font=FONT, bg=BGCHOICE, fg="white").pack()

class FinanceSolver(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        

class BoxPlot(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Box Plot", font=FONT, bg=BGCHOICE, fg="white")
        label.grid(row=0, column=0, pady=10)

        Button1 = tk.Button(self, text="Back", font=FONT, bg=WIDGETCOLOUR, command=lambda: parent.show_frame(SelectScreen))
        Button1.grid(row=1, column=0, pady=10)

        fig, ax = plt.subplots()
        x = np.random.normal(0, 1, 1000)
        ax.boxplot(x)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=2, column=0)

class Regression(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Regression", font=FONT, bg=BGCHOICE, fg="white")
        label.grid(row=0, column=0, pady=10)

        Button1 = tk.Button(self, text="Back", font=FONT, bg=WIDGETCOLOUR, command=lambda: parent.show_frame(SelectScreen))
        Button1.grid(row=1, column=0, pady=10)

        fig, ax = plt.subplots()
        x = np.random.normal(0, 1, 1000)
        y = 2*x + np.random.normal(0, 1, 1000)
        ax.scatter(x, y)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=2, column=0)

class Button(tk.Button):
    def __init__(self, parent, controller, cmd, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.configure(font=FONT, fg="black", bd=0, relief="flat", activeforeground="black")
        self.configure(bg=WIDGETCOLOUR, activebackground=WIDGETCOLOUR)


        if cmd == FUNC1:
            self.configure(command=lambda: controller.show_frame(AmortisationTable))
            self["text"] = FUNC1
        elif cmd == FUNC2:
            self.configure(command=lambda: controller.show_frame(FinanceSolver))
            self["text"] = FUNC2
        elif cmd == FUNC3:
            self.configure(command=lambda: controller.show_frame(BoxPlot))
            self["text"] = FUNC3
        elif cmd == FUNC4:
            self.configure(command=lambda: controller.show_frame(Regression))
            self["text"] = FUNC4


def generate(root):
    FunctionsWindow = FunctionsController(root)
    root.withdraw()
    FunctionsWindow.protocol("WM_DELETE_WINDOW", lambda: [FunctionsWindow.destroy(), root.deiconify()])
