#############################################################################################
#   File:       calculator.py                                                               #
#   Author:     R. Saluja                                                                   #
#   Date:       027/07/2024                                                                 #
#   Version:    1.0                                                                         #
#                                                                                           #
#   Description:                                                                            #
#   This file creates and runs the calculator window for the FM Calculator application.     #
#   It creates the window and places down the buttons in the calculator in a conventional   #
#   calculator grid.                                                                        #
#                                                                                           #
#   Naming Conventions:                                                                     #
#       - Classes: CamelCase (e.g., TkinterApp)                                             #
#       - Functions: CamelCase (e.g., AddToDisplay)                                         #
#       - Variables: CamelCase (e.g., FunctionsImg, CalculateButton)                        #
#############################################################################################

import tkinter as tk

# Constants
MAINTITLE = "Calculator"
BGCHOICE = "#353333"
WIDGETCOLOUR = "#D9D9D9"
FUNCWIDGET = "#CDBC9A"
NUMWIDGET = "#5F6465"
ANSWIDGET = "#D1A9D4"
FONT = ('Segoe UI', 20)

class Calculator(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        # Configure window
        self.title(MAINTITLE)
        self.focus_force()
        self.configure(bg=BGCHOICE)
        self.geometry("450x530")
        self.iconbitmap("assets/FMLogo.ico")
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

        Button(self, "func", "Clear", text="C").place(x=10, y=100, width=100, height=70)
        Button(self, "func", "del", text="del").place(x=120, y=100, width=100, height=70)
        Button(self, "func", "add", text="^").place(x=230, y=100, width=100, height=70)
        Button(self, "func", "add", text="+").place(x=340, y=100, width=100, height=70)

        tk.Label(self, text="* you can use your keyboard to input too! *", justify="center", bg=BGCHOICE, fg="white").place(x=0, y=495, width=450, height=20)
        tk.Label(self, text="* press esc or close the window to return back to the homepage! *", justify="center", bg=BGCHOICE, fg="white").place(x=0, y=510, width=450, height=20)

        # Bindings
        self.bind("<Return>", lambda event: Calculator.Calculate(Calculator, self.TopDisplay))
        self.bind("<BackSpace>", lambda event: Calculator.Delete(Calculator, self.TopDisplay))

        self.bind("<Escape>", lambda event: [self.destroy(), self.master.deiconify()])

        # bind the numbers on the keyboard
        self.bind("<KeyPress-0>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "0"))
        self.bind("<KeyPress-1>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "1"))
        self.bind("<KeyPress-2>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "2"))
        self.bind("<KeyPress-3>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "3"))
        self.bind("<KeyPress-4>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "4"))
        self.bind("<KeyPress-5>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "5"))
        self.bind("<KeyPress-6>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "6"))
        self.bind("<KeyPress-7>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "7"))
        self.bind("<KeyPress-8>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "8"))
        self.bind("<KeyPress-9>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "9"))
        self.bind("<KeyPress-period>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "."))
        self.bind("<KeyPress-plus>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "+"))
        self.bind("<KeyPress-minus>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "-"))
        self.bind("<KeyPress-asterisk>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "*"))
        self.bind("<KeyPress-slash>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "/"))
        self.bind("<KeyPress-asciicircum>", lambda event: Calculator.AddToDisplay(Calculator, self.TopDisplay, "^"))
        self.bind("<KeyPress-Return>", lambda event: Calculator.Calculate(Calculator, self.TopDisplay))
        self.bind("<KeyPress-BackSpace>", lambda event: Calculator.Delete(Calculator, self.TopDisplay))




    
    #########################################################################################
    #   Name:      AddToDisplay                                                             #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      27/07/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     entry                                                                    #        
    #   Output:    adds the users input the end of the entry with validation included.      #                        
    #   Return:    None                                                                     #      
    #########################################################################################
    def AddToDisplay(self, entry, value):
        entry.configure(state="normal")

        if entry.get() == "Error":
            entry.delete(0, tk.END)
        
        if value in ["+", "-", "*", "/", "^"] and entry.get()[-1] in ["+", "-", "*", "/", "^"]:	
            entry.delete(len(entry.get()) - 1)

        entry.insert(tk.END, value)
        entry.configure(state="readonly")
    
    #########################################################################################
    #   Name:      Clear                                                                    #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      27/07/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     entry                                                                    #        
    #   Output:    clears the entire entry                                                  #                        
    #   Return:    None                                                                     #      
    #########################################################################################
    def Clear(self, entry):
        entry.configure(state="normal")
        entry.delete(0, tk.END)
        entry.configure(state="readonly")

    #########################################################################################
    #   Name:      ChangeSign                                                               #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      27/07/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     entry                                                                    #        
    #   Output:    alternates between a + and - at the beginning of the entry               #                        
    #   Return:    None                                                                     #      
    #########################################################################################
    def ChangeSign(self, entry):
        entry.configure(state="normal")
        if entry.get()[0] == "-":
            entry.delete(0)
        else:
            entry.insert(0, "-")
        entry.configure(state="readonly")
    
    #########################################################################################
    #   Name:      Delete                                                                   #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      27/07/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     entry                                                                    #        
    #   Output:    deletes the last thing the user inputted into the entry                  #                        
    #   Return:    None                                                                     #      
    #########################################################################################
    def Delete(self, entry):
        entry.configure(state="normal")
        entry.delete(len(entry.get()) - 1)
        entry.configure(state="readonly")

    #########################################################################################
    #   Name:      Calculate                                                                #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      27/07/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     entry                                                                    #        
    #   Output:    changes the entry to the answer of the input provided or an error.       #                        
    #   Return:    None                                                                     #      
    #########################################################################################
    def Calculate(self, entry):
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
            self.configure(command=lambda: Calculator.ChangeSign(Calculator, self.master.TopDisplay))
        elif cmd == "Clear":
            self.configure(command=lambda: Calculator.Clear(Calculator, self.master.TopDisplay))
        elif cmd == "calculate":
            self.configure(command=lambda: Calculator.Calculate(Calculator, self.master.TopDisplay))
        elif cmd == "add":
            self.configure(command=lambda: Calculator.AddToDisplay(Calculator, self.master.TopDisplay, self["text"]))
        elif cmd == "del":
            self.configure(command=lambda: Calculator.Delete(Calculator, self.master.TopDisplay))


#########################################################################################
#   Name:      Generate                                                                 #        
#   Author:    R. Saluja                                                                #                
#   Date:      03/08/2024                                                               #        
#   Version:   1.0                                                                      #            
#   Input:     none                                                                     #        
#   Output:    opens this window and closes the main window.                            #                        
#   Return:    None                                                                     #            
#                                                                                       #    
#   Function exists to access the features of the calculator window upon the users      #
#   request.                                                                            #     
#########################################################################################
def Generate(root):
    CalculatorWindow = Calculator(root)
    root.withdraw()
    CalculatorWindow.protocol("WM_DELETE_WINDOW", lambda: [CalculatorWindow.destroy(), root.deiconify()])
