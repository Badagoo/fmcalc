#############################################################################################
#   File:       notepad.py                                                                  #                             
#   Author:     R. Saluja                                                                   #                    
#   Date:       02/07/2024                                                                  #    
#   Version:    1.0                                                                         #            
#                                                                                           #                
#   Description:                                                                            #            
#   This file creates the notepad window for the FM Calculator application. It creates the  #                                 
#   notepad window and places down the text area for the user to write notes. It also       #                                
#   creates the file bar with the title of the note and the save and load buttons. The save #
#   button saves the note to a file and the load button loads a note from a file. The save  #
#   The save button opens the save window if the note is untitled. The save window allows   #
#   the user to save the note to a file with a name and location specified by the user.     #
#                                                                                           #
#   Naming Conventions:                                                                     #
#       - Classes: CamelCase (e.g. SaveWindow)                                              #
#       - Functions: CamelCase (e.g. SaveNote)                                              #
#       - Variables: CamelCase (e.g. LoadButton)                                            #
#############################################################################################

import tkinter as tk
from tkinter import filedialog

# Constants
MAINTITLE = "Notepad"
SAVETITLE = "Save"
LOADTITLE = "Load"
BGCHOICE = "#353333"
WIDGETCOLOUR = "#D9D9D9"
FONT = ('Segoe UI', 15)

class Notepad(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        # Load Images
        SaveImg = tk.PhotoImage(file='assets\save.png')
        LoadImg = tk.PhotoImage(file='assets\load.png')

        # Configure window
        self.title(MAINTITLE)
        self.focus_force()
        self.configure(bg=BGCHOICE)
        self.geometry("650x350")
        self.iconbitmap("assets\FMLogo.ico")
        self.resizable(False, False)
        self.bind("<Escape>", lambda event: [self.destroy(), self.master.deiconify()])

        # text area
        self.TextArea = tk.Text(self, font=FONT, bg=WIDGETCOLOUR, bd=0)
        self.TextArea.place(x=10, y=40, width=630, height=300)

        # File Bar
        TitleBar = tk.Label(self, font=FONT, text="Untitled*", bg=WIDGETCOLOUR, bd=0)
        TitleBar.place(x=10, y=10, width=200, height=30)

        # Save Button
        SaveButton = tk.Button(self,
                                borderwidth=0,
                                bg=WIDGETCOLOUR,
                                image=SaveImg,
                                command=lambda: SaveNote()
                                )
        SaveButton.image = SaveImg # call this to prevent garbage collection

        # Load Button
        LoadButton = tk.Button(self,
                                borderwidth=0,
                                bg=WIDGETCOLOUR,
                                image=LoadImg,
                                command=lambda: LoadNote()
                                )
        LoadButton.image = LoadImg # call this to prevent garbage collection

        # Place buttons on the screen
        SaveButton.place(x=580, y=10, width=30, height=30)
        LoadButton.place(x=610, y=10, width=30, height=30)

        #########################################################################################
        #   Name:      LoadNote                                                                 #        
        #   Author:    R. Saluja                                                                #                
        #   Date:      02/07/2024                                                               #        
        #   Version:   1.0                                                                      #            
        #   Input:     None                                                                     #        
        #   Output:    Populates the text area with the text from the file                      #                        
        #   Return:    None                                                                     #            
        #                                                                                       #    
        #   Function exists for the user to load a note from the file. It opens a file dialog   #        
        #   box for the user to select a file and populates the text area with the text from    #    
        #   the file. It also changes the title bar to the name of the file.                    #    
        #########################################################################################
        def LoadNote():
            file = filedialog.askopenfile(filetypes=[("Text files", "*.txt")])
            if file is not None:
                content = file.read()
                self.TextArea.delete("1.0", "end")
                self.TextArea.insert("1.0", content)
                TitleBar.config(text=file.name.split("/")[-1][:-4])

                # Get the location of the file for saving later if necessary
                CurrentLocation = file.name
                CurrentLocation = CurrentLocation.replace(file.name.split("/")[-1], "")

        #########################################################################################
        #   Name:      SaveNote                                                                 #    
        #   Author:    R. Saluja                                                                #                
        #   Date:      02/07/2024                                                               #            
        #   Version:   1.0                                                                      #    
        #   Input:     None                                                                     #    
        #   Output:    Saves the note to the file or opens the save window                      #                            
        #   Return:    None                                                                     #        
        #                                                                                       #    
        #   Function exists for the user to save the text from the notepad into the file        #                
        #   or open the save window if the note is untitled. It checks if the note is untitled  #            
        #   and opens the save window if it is. If the note has a title, it saves the note      #        
        #   into the file with the same name.                                                   #    
        #########################################################################################
        def SaveNote():
            if TitleBar.cget("text") == "Untitled*":
                SaveWindow(self.TextArea.get("1.0", "end"), TitleBar)
            else:
                CurrentLocation = filedialog.askdirectory(initialdir="\\notes", title="Select a location")
                with open(f"{CurrentLocation}\\{TitleBar.cget('text')}.txt", "w") as file:
                    file.write(self.TextArea.get("1.0", "end"))

    
class SaveWindow(Notepad):
    def __init__(self, note, name, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.note = note

        # Load Images
        FolderImg = tk.PhotoImage(file='assets/folder.png')

        # Configure window
        self.title(SAVETITLE)
        self.focus_force()
        self.configure(bg=BGCHOICE)
        self.geometry("400x220")
        self.iconbitmap("assets/FMLogo.ico")
        self.resizable(False, False)

        # Entry for the file name
        FileNameEntry = tk.Entry(self, font=FONT, fg="grey", bg=WIDGETCOLOUR, bd=0)
        FileNameEntry.place(x=10, y=10, width=320, height=50)

        FileNameExtensionLabel = tk.Label(self, text=".txt", font=FONT, bg=WIDGETCOLOUR, bd=0)
        FileNameExtensionLabel.place(x=330, y=10, width=60, height=50)

        # Entry for the location
        LocationEntry = tk.Entry(self, font=FONT, fg="grey", bg=WIDGETCOLOUR, bd=0)
        LocationEntry.place(x=10, y=70, width=320, height=50)

        LocationEntryButton = tk.Button(self, image=FolderImg, font=FONT, bg=WIDGETCOLOUR, bd=0, command=lambda: SelectLocation())
        LocationEntryButton.image = FolderImg
        LocationEntryButton.place(x=330, y=70, width=60, height=50)

        # Save Button
        SaveButton = tk.Button(self, text="Save", font=FONT, bg=WIDGETCOLOUR, bd=0, command=lambda: SaveFile())
        SaveButton.place(x=10, y=150, width=380, height=50)

        # Placeholder text
        LocationEntry.insert(0, "Location")
        LocationEntry.bind("<FocusIn>", lambda event: FocusEntry(LocationEntry))
        LocationEntry.bind("<FocusOut>", lambda event: UnfocusEntry(LocationEntry, "Location"))

        FileNameEntry.insert(0, "Name")
        FileNameEntry.bind("<FocusIn>", lambda event: FocusEntry(FileNameEntry))
        FileNameEntry.bind("<FocusOut>", lambda event: UnfocusEntry(FileNameEntry, "Name"))

        #########################################################################################
        #   Name:      SaveFile                                                                 #        
        #   Author:    R. Saluja                                                                #                
        #   Date:      02/07/2024                                                               #            
        #   Version:   1.0                                                                      #            
        #   Input:     None                                                                     #            
        #   Output:    Textfile in the selected location with the text from the notepad         #                        
        #   Return:    None                                                                     #        
        #                                                                                       #    
        #   Function exists for the user to save the text from the notepad into a textfile.     #                    
        #   It opens a file dialog box for the user to select a location and saves the text     #                            
        #   into a textfile with the name specified by the user.                                #        
        #########################################################################################
        def SaveFile():
            try:
                with open(f"{LocationEntry.get()}/{FileNameEntry.get()}.txt", "w") as file:
                    file.write(self.note)
                name.config(text=FileNameEntry.get())
                self.destroy()
            except FileNotFoundError:
                pass

        #########################################################################################
        #   Name:      SelectLocation                                                           #                                    
        #   Author:    R. Saluja                                                                #                                
        #   Date:      02/07/2024                                                               #                                
        #   Version:   1.0                                                                      #                        
        #   Input:     None                                                                     #                        
        #   Output:    Changes the text in the entry to the selected location                   #                                                                            
        #   Return:    None                                                                     #                        
        #                                                                                       #        
        #   Function exists for the user to select a location to save the file. It opens        #                                                                                        
        #   a file dialog box for the user to select a location and changes the text in the     #                                                                                        
        #   entry to the selected location.                                                     #                                        
        #########################################################################################
        def SelectLocation():
            Location = filedialog.askdirectory(initialdir="./notes", title="Select a location")
            LocationEntry.config(fg="black")
            LocationEntry.delete(0, "end")
            LocationEntry.insert(0, Location)

        #########################################################################################
        #   Name:      FocusEntry                                                               #
        #   Author:    R. Saluja                                                                #      
        #   Date:      02/07/2024                                                               #         
        #   Version:   1.0                                                                      #    
        #   Input:     Object: Entry (The entry to be modified)                                 #                                 
        #   Output:    Deletes text in the entry and changes the text colour to black           #                                                    
        #   Return:    None                                                                     #
        #                                                                                       #    
        #   Function exists to delete the placeholder text for the user to enter their          #                                                    
        #   own text. It also changes the text colour to black to indicate that the user        #                                                        
        #   can now enter their text.                                                           #    
        #########################################################################################
        def FocusEntry(Object):
            if Object.get() == "Name" or Object.get() == "Location":
                Object.delete(0, "end")
                Object.config(fg="black")

        #########################################################################################
        #   Name:      UnfocusEntry                                                             #
        #   Author:    R. Saluja                                                                #
        #   Date:      02/07/2024                                                               #
        #   Version:   1.0                                                                      #
        #   Input:     Object: Entry (The entry to be modified)                                 #
        #   Input:     Text: String (The placeholder text)                                      #
        #   Output:    Deletes text in the entry and changes the text colour to black           #
        #   Return:    None                                                                     #
        #                                                                                       #
        #   Function exists to add the placeholder text back into the entry if the user         #
        #   has not entered any text. It also changes the text colour to grey to indicate       #
        #   that the text is a placeholder.                                                     #
        #########################################################################################
        def UnfocusEntry(Object, Text):
            if Object.get() == "":
                Object.insert(0, Text)
                Object.config(fg="grey")


#########################################################################################
#   Name:      Generate                                                                 #        
#   Author:    R. Saluja                                                                #                
#   Date:      03/08/2024                                                               #        
#   Version:   1.0                                                                      #            
#   Input:     none                                                                     #        
#   Output:    opens this window and closes the main window.                            #                        
#   Return:    None                                                                     #            
#                                                                                       #    
#   Function exists to access the features of the notepad window upon the users         #
#   request.                                                                            #     
#########################################################################################
def Generate(root):
    NotepadWindow = Notepad(root)
    root.withdraw()
    NotepadWindow.protocol("WM_DELETE_WINDOW", lambda: [NotepadWindow.destroy(), root.deiconify()])