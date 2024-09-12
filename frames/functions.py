#############################################################################################
#   File:       functions.py                                                                #
#   Author:     R. Saluja                                                                   #
#   Date:       10/09/2024                                                                  #
#   Version:    1.0                                                                         #
#                                                                                           #
#   Description:                                                                            #
#   This file creates and runs the functions page for the FM Calculator application.        #
#   It creates the window and places down the buttons in the functions controller for the   #
#   user to access whichever calculator they want                                           #
#                                                                                           #
#   Naming Conventions:                                                                     #
#       - Classes: CamelCase (e.g., TkinterApp)                                             #
#       - Functions: CamelCase (e.g., ShowFrame)                                            #
#       - Variables: CamelCase (e.g., FunctionsImg, CalculateButton)                        #
#############################################################################################

import tkinter as tk
from tkinter import messagebox

#########################################################################################
#   Name:      PaymentError                                                             #        
#   Author:    R. Saluja                                                                #                
#   Date:      03/08/2024                                                               #        
#   Version:   1.0                                                                      #            
#   Input:     none                                                                     #        
#   Output:    messagebox containing an error message                                   #                        
#   Return:    None                                                                     #            
#                                                                                       #    
#   Function exists to warn the user that they cannot access a feature due to not       #
#   an active subscription.                                                             #     
#########################################################################################
def PaymentError():
    messagebox.showerror("Payment Error", "Subscribe to access this feature!")

MAINTITLE = "Functions"
FUNC1 = "Determinant"
FUNC2 = "Finance"
FUNC3 = "Box Plot"
FUNC4 = "Standardised"
BGCHOICE = "#353333"
WIDGETCOLOUR = "#D9D9D9"
FONT = ('Segoe UI', 15)

class FunctionsController(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.title(MAINTITLE)
        self.geometry("375x400")
        self.iconbitmap("assets\FMLogo.ico")
        self.resizable(False, False)
        self.focus_force()
        self.bind("<Escape>", lambda event: [self.destroy(), self.master.deiconify()])

        self.frames = {}

        for F in (SelectScreen, Determinant, Finance, BoxPlot, StandardisedScores):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.ShowFrame(SelectScreen)

    #########################################################################################
    #   Name:      ShowFrame                                                                #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      03/08/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     cont                                                                     #        
    #   Output:    changes the frame of the window to the inputted frame.                   #                        
    #   Return:    None                                                                     #            
    #                                                                                       #    
    #   Function exists in the controller to modify the frame dependant on whichever button #
    #   the user presses and the button sends the content to this function.                 #     
    #########################################################################################
    def ShowFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class SelectScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.configure(width=375, height=375, bg=BGCHOICE)

        Button(self, parent, FUNC1).place(x=25, y=25, width=150, height=150)
        Button(self, parent, FUNC2).place(x=200, y=25, width=150, height=150)
        Button(self, parent, FUNC3).place(x=25, y=200, width=150, height=150)
        Button(self, parent, FUNC4).place(x=200, y=200, width=150, height=150)

class Determinant(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.configure(width=375, height=400, bg=BGCHOICE)

        tk.Label(self, text="Enter the values of the matrix", font=FONT, bg=WIDGETCOLOUR).place(x=25, y=25, width=325, height=30)

        self.InputA = tk.Entry(self, font=FONT, bg=WIDGETCOLOUR, bd=0, justify='center')
        self.InputA.place(x=75, y=75, width=100, height=100)
        self.InputB = tk.Entry(self, font=FONT, bg=WIDGETCOLOUR, bd=0, justify='center')
        self.InputB.place(x=200, y=75, width=100, height=100)
        self.InputC = tk.Entry(self, font=FONT, bg=WIDGETCOLOUR, bd=0, justify='center')
        self.InputC.place(x=75, y=200, width=100, height=100)
        self.InputD = tk.Entry(self, font=FONT, bg=WIDGETCOLOUR, bd=0, justify='center')
        self.InputD.place(x=200, y=200, width=100, height=100)

        tk.Button(self, text="solve", font=FONT, bg=WIDGETCOLOUR, command=self.SolveDeterminant).place(x=25, y=325, width=325, height=30)

    #########################################################################################
    #   Name:      SolveDeterminant                                                         #        
    #   Author:    R. Saluja                                                                #                
    #   Date:      03/08/2024                                                               #        
    #   Version:   1.0                                                                      #            
    #   Input:     none                                                                     #        
    #   Output:    generates a label with the determinant that is calculated.               #                        
    #   Return:    None                                                                     #            
    #                                                                                       #    
    #   Function exists to plug in the user inputs from the entry into a formula for        #
    #   calculating the determinant of a 2x2 matrix.                                        #     
    #########################################################################################
    def SolveDeterminant(self):
        try:
            A = int(self.InputA.get())
            D = int(self.InputD.get())
            B = int(self.InputB.get())
            C = int(self.InputC.get())
            Determinant = (A * D) - (B * C)
            tk.Label(self, text=Determinant, font=FONT, bg=BGCHOICE, fg="white").place(x=25, y=370, width=325, height=20)
        except: 
            messagebox.showerror("Value Error", "Make sure every entry has only numbers in it!")


class Finance(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

class BoxPlot(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)    

class StandardisedScores(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


class Button(tk.Button):
    def __init__(self, parent, controller, cmd, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.configure(font=FONT, fg="black", bd=0, relief="flat", activeforeground="black")
        self.configure(bg=WIDGETCOLOUR, activebackground=WIDGETCOLOUR)


        if cmd == FUNC1:
            self.configure(command=lambda: controller.ShowFrame(Determinant))
            self["text"] = FUNC1
        elif cmd == FUNC2:
            self.configure(command=lambda: PaymentError())
            self["text"] = FUNC2
        elif cmd == FUNC3:
            self.configure(command=lambda: PaymentError())
            self["text"] = FUNC3
        elif cmd == FUNC4:
            self.configure(command=lambda: PaymentError())
            self["text"] = FUNC4

#########################################################################################
#   Name:      Generate                                                                 #        
#   Author:    R. Saluja                                                                #                
#   Date:      03/08/2024                                                               #        
#   Version:   1.0                                                                      #            
#   Input:     none                                                                     #        
#   Output:    opens this window and closes the main window.                            #                        
#   Return:    None                                                                     #            
#                                                                                       #    
#   Function exists to access the features of the functions window upon the users       #
#   request.                                                                            #     
#########################################################################################
def Generate(root):
    FunctionsWindow = FunctionsController(root)
    root.withdraw()
    FunctionsWindow.protocol("WM_DELETE_WINDOW", lambda: [FunctionsWindow.destroy(), root.deiconify()])

