#############################################################################################
#   File:       main.py                                                                     #
#   Author:     R. Saluja                                                                   #
#   Date:       02/07/2024                                                                  #
#   Version:    1.0                                                                         #
#                                                                                           #
#   Description:                                                                            #
#   This file creates and runs the homepage for the FM Calculator application. It creates   #
#   It creates the window and places down the buttons for the calculator, notepad, and      #
#   functions. The buttons are placed in a grid layout and are linked to their respective   #
#   functions.                                                                              #
#                                                                                           #
#   Naming Conventions:                                                                     #
#       - Classes: CamelCase (e.g., TkinterApp)                                             #
#       - Functions: none                                                                   #
#       - Variables: CamelCase (e.g., FunctionsImg, CalculateButton)                        #
#############################################################################################

import tkinter as tk
import frames.calculator as calculator
import frames.notepad as notepad
import frames.functions as functions

# constants
TITLE = "FM CALCULATOR"
BGCHOICE = "#353333"
BUTTONCOLOUR = "#D9D9D9"
FOLDER = "assets"


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Load images
        CalculateImg = tk.PhotoImage(file=f'{FOLDER}/calculate.png')
        NotepadImg = tk.PhotoImage(file=f'{FOLDER}/notepad.png')
        FunctionsImg = tk.PhotoImage(file=f'{FOLDER}/functions.png')

        # Configure window
        self.title(TITLE)
        self.configure(bg=BGCHOICE)
        self.geometry("650x350")
        self.iconbitmap(f"{FOLDER}/FMLogo.ico")
        self.resizable(False, False)

        # Create buttons
        CalculatorButton = tk.Button(self,
                                    borderwidth=0,
                                    bg=BUTTONCOLOUR,
                                    image=CalculateImg,
                                    command=lambda: calculator.generate(self))
        CalculatorButton.image = CalculateImg # call this to prevent garbage collection

        NotepadButton = tk.Button(self,
                                    borderwidth=0,
                                    bg=BUTTONCOLOUR,
                                    image=NotepadImg,
                                    command=lambda: notepad.generate(self))
        NotepadButton.image = NotepadImg # call this to prevent garbage collection

        FunctionsButton = tk.Button(self,
                                    borderwidth=0,
                                    bg=BUTTONCOLOUR,
                                    image=FunctionsImg,
                                    command=lambda: functions.generate(self))
        FunctionsButton.image = FunctionsImg # call this to prevent garbage collection

        # Place buttons on the screen
        CalculatorButton.place(x=25, y=25, width=180, height=300)
        NotepadButton.place(x=235, y=25, width=180, height=300)
        FunctionsButton.place(x=450, y=25, width=180, height=300)

# Driver Code
App().mainloop()
