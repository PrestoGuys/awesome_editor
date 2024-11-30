# Awesome Editor v0.0.2 - A simple editor made in Python3 with Tk
# Copyright (C) 2024  PrestoGuys
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import yaml

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from disclaimer import *
from ccp import cut, copy, paste
from open_file import openfile
from disclaimer_file import disclaimer_file
from manual import manual


class TextEditor:
    def __init__(self, root):
        print_disclaimer()  # Prints the opening warrenty disclaimer


        # Opens the config file and saves it in a variable
        with open('config/config.yaml', 'r') as file:
            config_json = yaml.load(file, Loader=yaml.FullLoader)


        editor_font = config_json['Font']['Editor_Font']  # Gets editor's font
        editor_font_size = config_json['Font']['Editor_Font_Size']  # Gets editor's font size

        background_color = config_json['Color']['Editor_Color']  # Gets editor's background color
        foreground_color = config_json['Color']['Editor_Font_Color']  # Gets editor's foreground color


        self.root = root # Assigns root

        # CHANGE THIS!!!! THERE IS MUTCH BETTER WAY THAT PROPERLY CENTERS HERE!: https://stackoverflow.com/a/10018670
        window_width = 1150  # Set the width of the window
        window_height = 800  # Set the height of the window
        screen_width = self.root.winfo_screenwidth()  # Get the screen's width
        screen_height = self.root.winfo_screenheight()  # Get the screen's height
        center_x = int(screen_width / 2 - window_width / 2)  # Calculate the x and y coordinates for the window to be centered
        center_y = int(screen_height / 2 - window_height / 2)  # Calculate the x and y coordinates for the window to be centered

        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")  # Set the geometry of the window with the calculated positions


        icon = PhotoImage(file="assets/graphics/icon.png")  # Opens icon file and saves it to a variable
        root.iconphoto(True, icon)  # Sets icon


        self.root.config(bg=background_color)  # Set background with backgroun_color
        self.filename = None  # Initialize filename
        self.title = StringVar()  # Declare title variable
        self.status = StringVar()  # Declare status variable


        self.info_bar = Label(self.root, textvariable=self.title, font=("sans-serif", 10), bd=2, anchor="w", relief=GROOVE)  # Creating info_bar
        self.info_bar.pack(side=BOTTOM, fill=BOTH)  # Packing info_bar to root window
        self.settitle("Welcome to Awesome Editor v0.0.2")  # Calling Settitle Function


        self.menubar = Menu(self.root, font=("sans-serif", 10), activebackground="#aaaaaa")  # Creating Menubar
        self.root.config(menu=self.menubar)  # Configuring menubar on root window

        # Adding file menu to menubar
        self.filemenu = Menu(self.menubar, font=("sans-serif", 10), activebackground="#aaaaaa", tearoff=0)  # Creating File Menu
        self.filemenu.add_command(label="New", accelerator="Ctrl+N", command=self.newfile)  # Adding New file Command
        self.filemenu.add_command(label="Open", accelerator="Ctrl+O", command=lambda: openfile(self.txtarea, self.settitle))  # Adding Open file Command
        self.filemenu.add_command(label="Save", accelerator="Ctrl+S", command=self.savefile)  # Adding Save File Command
        self.filemenu.add_command(label="Save As", accelerator="Ctrl+A", command=self.saveasfile)  # Adding Save As file Command
        self.filemenu.add_separator()  # Adding Seprator
        self.filemenu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit)  # Adding Exit window Command
        self.menubar.add_cascade(label="File", menu=self.filemenu)  # Cascading filemenu to menubar

        # Adding edit menu to menubar
        self.editmenu = Menu(self.menubar, font=("sans-serif", 10), activebackground="#aaaaaa", tearoff=0)  # Creating Edit Menu
        self.editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: cut(self.txtarea))  # Adding Cut text Command
        self.editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: copy(self.txtarea))  # Adding Copy text Command
        self.editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: paste(self.txtarea))  # Adding paste text Command
        self.editmenu.add_separator()  # Adding Seprator
        self.editmenu.add_command(label="Undo", accelerator="Ctrl+U", command=self.undo)  # Adding Undo text Command
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)  # Cascading editmenu to menubar

        # Adding help menu to menubar
        self.helpmenu = Menu(self.menubar, font=("sans-serif", 10), activebackground="#aaaaaa", tearoff=0)  # Creating Help Menu
        self.helpmenu.add_command(label="About", command=self.infoabout)  # Adding About Command
        self.helpmenu.add_command(label="Manual", command=lambda: manual(self.txtarea, self.title, self.root, self.settitle))  # Adding Manual Command
        self.helpmenu.add_separator()  # Adding Seprator
        self.helpmenu.add_command(label="License", command=self.licenseread)  # Adding License Command
        self.helpmenu.add_command(label="Disclaimer", command=lambda: disclaimer_file(self.txtarea, self.title, self.root, self.settitle))  # Adding Disclaimer Command
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)  # Cascading helpmenu to menubar


        scrol_y = Scrollbar(self.root, orient=VERTICAL)  # Creating Scrollbar


        self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=(editor_font, editor_font_size), state="normal",
                            relief=GROOVE, bg=background_color, fg=foreground_color, borderwidth=0)  # Text part of the editor


        scrol_y.pack(side=RIGHT, fill=Y)  # Packing scrollbar to root window
        scrol_y.config(command=self.txtarea.yview)  # Adding Scrollbar to text area
        self.txtarea.pack(fill=BOTH, expand=1)  # Packing Text Area to root window

        self.shortcuts()  # Calling shortcuts funtion


    # Sets title of window and status bar, e.g. "Awesome Editor v0.0.2 - Untitled"
    def settitle(self, status):
        # Checking if Filename is not None
        if self.filename:
            titlefile = self.filename  # Updating Title as filename

        else:
            titlefile = "Untitled"  # Updating Title as Untitled
            # self.root.title('Awesome Editor v0.0.2' + ' - ' + titlefile)   (IDK WHY I COMMENTED THIS OUT, I LEAVE IT IN.)

        self.title.set(status + " | " + titlefile)


    # Defining New file Function
    def newfile(self, *args):
        self.txtarea.config(state='normal')
        self.txtarea.delete("1.0", END)  # Clearing the Text Area
        self.filename = None  # Updating filename as None
        self.settitle(" ")  # Calling settitle funtion
        self.settitle("New File Created")  # updating status


    # Defining Save File Funtion
    def savefile(self, *args):
        self.txtarea.config(state='normal')
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Reading the data from text area
                data = self.txtarea.get("1.0", END)
                # opening File in write mode
                outfile = open(self.filename, "w")
                # Writing Data into file
                outfile.write(data)
                # Closing File
                outfile.close()
                # Calling Set title
                self.settitle(" ")
                # Updating Status
                self.settitle("Saved Successfully")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception", e)

    # Defining Save As File Funtion
    def saveasfile(self, *args):
        self.txtarea.config(state='normal')
        # Exception handling
        try:
            # Asking for file name and type to save
            untitledfile = filedialog.asksaveasfilename(title="Save file As", defaultextension=".txt",
                                                        initialfile="Untitled.txt", filetypes=(
                    ("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
            # Reading the data from text area
            data = self.txtarea.get("1.0", END)
            # opening File in write mode
            outfile = open(untitledfile, "w")
            # Writing Data into file
            outfile.write(data)
            # Closing File
            outfile.close()
            # Updating filename as Untitled
            self.filename = untitledfile
            # Calling Set title
            self.settitle(" ")
            # Updating Status
            self.settitle("Saved Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    # Defining Exit Funtion
    def exit(self, *args):
        op = messagebox.askyesno("Exit Warning", "Your unsaved work will be lost!")
        if op > 0:
            self.root.destroy()
        else:
            return

    # Defining Undo Funtion
    def undo(self, *args):
        self.txtarea.config(state='normal')
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Clearing Text Area
                self.txtarea.delete("1.0", END)
                # opening File in read mode
                infile = open(self.filename, "r")
                # Inserting data Line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing File
                infile.close()
                # Calling Set title
                self.settitle(" ")
                # Updating Status
                self.settitle("Undone Successfully")
            else:
                # Clearing Text Area
                self.txtarea.delete("1.0", END)
                # Updating filename as None
                self.filename = None
                # Calling Set title
                self.settitle(" ")
                # Updating Status
                self.settitle("Undone Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

    # Defining About Funtion
    def infoabout(self):
        messagebox.showinfo("About Awesome Editor",
                            "Awesome Editor\n v0.0.2\nMade By PrestoGuys in 2024\nLicense: https://www.gnu.org/licenses/gpl-3.0.txt")





    def gghe(self):
        print("Hello, World!")







    def licenseread(self):
        self.txtarea.config(state='normal')
        # opening file in readmode
        infile = open('assets/texts/license.txt', "r")
        # Clearing text area
        self.txtarea.delete("1.0", END)
        # Inserting data Line by line into text area
        for line in infile:
            self.txtarea.insert(END, line)

        self.txtarea.config(state='disabled')

        self.title.set('License')
        self.root.title('Awesome Editor - License')

        self.settitle("Opened GNU GPL 3 License")


    # binds key shortcuts
    def shortcuts(self):
        # Binding Ctrl+n to newfile function
        self.txtarea.bind("<Control-n>", self.newfile)
        # Binding Ctrl+o to openfile function
        self.txtarea.bind("<Control-o>", lambda: openfile(self.txtarea, self.settitle))
        # Binding Ctrl+s to savefile function
        self.txtarea.bind("<Control-s>", self.savefile)
        # Binding Ctrl+a to saveasfile function
        self.txtarea.bind("<Control-a>", self.saveasfile)
        # binding ctrl+a to exit function
        self.txtarea.bind("<Control-q>", self.exit)

        self.txtarea.bind("<Control-u>", self.undo)


root = Tk()  # creating TK container
TextEditor(root)  # passing root to text editor class
root.mainloop()  # root window loop
