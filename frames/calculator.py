import tkinter as tk

# Current Errors
# cannot multiply by negatives due to the list in list
# can have multiple decimals in the same number when you shouldnt be able to
# some keybinds dont work
# when an error occurs, the error message sometimes doesnt happen and allows for the entry to be typed in
# code needs to be commented
# unable to open files with the calculator currently

# Constants
MAINTITLE = "Calculator"
BGCHOICE = "#353333"
WIDGETCOLOUR = "#D9D9D9"
FUNCWIDGET = "#CDBC9A"
NUMWIDGET = "#5F6465"
ANSWIDGET = "#D1A9D4"
FONT = "Segoe_UI 20"

class Calculator(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        # Configure window
        self.title(MAINTITLE)
        self.focus_force()
        self.configure(bg=BGCHOICE)
        self.geometry("450x500")
        self.iconbitmap("assets\FMLogo.ico")
        self.resizable(False, False)

        # Create display
        self.TopDisplay = tk.Entry(self, font=FONT, bg=WIDGETCOLOUR, fg="black", bd=0, relief="flat", justify="right", state="readonly")
        self.TopDisplay.place(x=10, y=10, width=430, height=70)

        # Create widgets
        Button(self, "num", "sign", text="+/-").place(x=10, y=420, width=100, height=70)
        Button(self, "num", "add", text="0").place(x=120, y=420, width=100, height=70)
        Button(self, "num", "add", text=".").place(x=230, y=420, width=100, height=70)
        Button(self, "ans", "calculate", text="=").place(x=340, y=420, width=100, height=70)

        Button(self, "num", "add", text="1").place(x=10, y=340, width=100, height=70)
        Button(self, "num", "add", text="2").place(x=120, y=340, width=100, height=70)
        Button(self, "num", "add", text="3").place(x=230, y=340, width=100, height=70)
        Button(self, "func", "add", text="/").place(x=340, y=340, width=100, height=70)

        Button(self, "num", "add", text="4").place(x=10, y=260, width=100, height=70)
        Button(self, "num", "add", text="5").place(x=120, y=260, width=100, height=70)
        Button(self, "num", "add", text="6").place(x=230, y=260, width=100, height=70)
        Button(self, "func", "add", text="*").place(x=340, y=260, width=100, height=70)

        Button(self, "num", "add", text="7").place(x=10, y=180, width=100, height=70)
        Button(self, "num", "add", text="8").place(x=120, y=180, width=100, height=70)
        Button(self, "num", "add", text="9").place(x=230, y=180, width=100, height=70)
        Button(self, "func", "add", text="-").place(x=340, y=180, width=100, height=70)

        Button(self, "func", "clear", text="C").place(x=10, y=100, width=100, height=70)
        Button(self, "func", "del", text="del").place(x=120, y=100, width=100, height=70)
        Button(self, "func", "add", text="^").place(x=230, y=100, width=100, height=70)
        Button(self, "func", "add", text="+").place(x=340, y=100, width=100, height=70)


        
        # Bindings
        self.bind("<Return>", lambda event: Calculator.calculate(Calculator, self.display))
        self.bind("<BackSpace>", lambda event: Calculator.delete(Calculator, self.display))

        self.bind("<Escape>", lambda event: [self.destroy(), self.master.deiconify()])

        # bind the numbers on the keyboard
        self.bind("<KeyPress-0>", lambda event: Calculator.add_to_display(Calculator, self.display, "0"))
        self.bind("<KeyPress-1>", lambda event: Calculator.add_to_display(Calculator, self.display, "1"))
        self.bind("<KeyPress-2>", lambda event: Calculator.add_to_display(Calculator, self.display, "2"))
        self.bind("<KeyPress-3>", lambda event: Calculator.add_to_display(Calculator, self.display, "3"))
        self.bind("<KeyPress-4>", lambda event: Calculator.add_to_display(Calculator, self.display, "4"))
        self.bind("<KeyPress-5>", lambda event: Calculator.add_to_display(Calculator, self.display, "5"))
        self.bind("<KeyPress-6>", lambda event: Calculator.add_to_display(Calculator, self.display, "6"))
        self.bind("<KeyPress-7>", lambda event: Calculator.add_to_display(Calculator, self.display, "7"))
        self.bind("<KeyPress-8>", lambda event: Calculator.add_to_display(Calculator, self.display, "8"))
        self.bind("<KeyPress-9>", lambda event: Calculator.add_to_display(Calculator, self.display, "9"))
        self.bind("<KeyPress-period>", lambda event: Calculator.add_to_display(Calculator, self.display, "."))
        self.bind("<KeyPress-plus>", lambda event: Calculator.add_to_display(Calculator, self.display, "+"))
        self.bind("<KeyPress-minus>", lambda event: Calculator.add_to_display(Calculator, self.display, "-"))
        self.bind("<KeyPress-asterisk>", lambda event: Calculator.add_to_display(Calculator, self.display, "*"))
        self.bind("<KeyPress-slash>", lambda event: Calculator.add_to_display(Calculator, self.display, "/"))
        self.bind("<KeyPress-asciicircum>", lambda event: Calculator.add_to_display(Calculator, self.display, "^"))
        self.bind("<KeyPress-Return>", lambda event: Calculator.calculate(Calculator, self.display))
        self.bind("<KeyPress-BackSpace>", lambda event: Calculator.delete(Calculator, self.display))




    def add_to_display(self, entry, value):
        entry.configure(state="normal")

        if entry.get() == "Error":
            entry.delete(0, tk.END)
        
        if value in ["+", "-", "*", "/", "^"] and entry.get()[-1] in ["+", "-", "*", "/", "^"]:	
            entry.delete(len(entry.get()) - 1)

        entry.insert(tk.END, value)
        entry.configure(state="readonly")

    def clear(self, entry):
        entry.configure(state="normal")
        entry.delete(0, tk.END)
        entry.configure(state="readonly")

    def change_sign(self, entry):
        entry.configure(state="normal")
        if entry.get()[0] == "-":
            entry.delete(0)
        else:
            entry.insert(0, "-")
        entry.configure(state="readonly")
    
    def delete(self, entry):
        entry.configure(state="normal")
        entry.delete(len(entry.get()) - 1)
        entry.configure(state="readonly")

    def calculate(self, entry):
        try:
            expression = entry.get()
            expression = expression.replace("^", "**")
            expression = expression.replace("√", "math.sqrt")
            entry.configure(state="normal")
            entry.delete(0, tk.END)
            ans = eval(expression)
            if ans % 1 == 0:
                ans = int(ans)
            entry.insert(tk.END, ans)
            entry.configure(state="readonly")
        except Exception as e:
            entry.configure(state="normal")
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            entry.configure(state="readonly")






class Button(tk.Button):
    def __init__(self, parent, buttontype, cmd, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.configure(font=FONT, fg="white", bd=0, relief="flat", activeforeground="white")
        if buttontype == "func":
            self.configure(bg=FUNCWIDGET, activebackground=FUNCWIDGET)
        elif buttontype == "num":
            self.configure(bg=NUMWIDGET, activebackground=NUMWIDGET)
        elif buttontype == "ans":
            self.configure(bg=ANSWIDGET, activebackground=ANSWIDGET)

        if cmd == "sign":
            self.configure(command=lambda: Calculator.change_sign(Calculator, self.master.display))
        elif cmd == "clear":
            self.configure(command=lambda: Calculator.clear(Calculator, self.master.display))
        elif cmd == "calculate":
            self.configure(command=lambda: Calculator.calculate(Calculator, self.master.display))
        elif cmd == "add":
            self.configure(command=lambda: Calculator.add_to_display(Calculator, self.master.display, self["text"]))
        elif cmd == "del":
            self.configure(command=lambda: Calculator.delete(Calculator, self.master.display))



def generate(root):
    CalculatorWindow = Calculator(root)
    root.withdraw()
    CalculatorWindow.protocol("WM_DELETE_WINDOW", lambda: [CalculatorWindow.destroy(), root.deiconify()])
