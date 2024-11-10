# Awesome Editor v0.0.1 - A simple editor made in Python3 with Tk
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


import json

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from disclaim import *


class TextEditor:
    def __init__(self, root):
        disclaim()

        bgcolor = None
        fgcolor = None

        # opens the config file and saves it in a variable
        with open('config/config.json', 'r') as file:
            data = json.load(file)

        configtheme = "light"
        configfont = data['Editor_Font']  # gets editor font
        textboxfontsize = data['Editor_Font_Size']  # gets editor font size

        bgcolor = data['Editor_Color']
        fgcolor = data['Editor_Font_Color']

        # assigns root
        self.root = root

        # window width and window height of the program
        window_width = 1100
        window_height = 780

        # gets screen_width and screen_height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # gets senter of the screen
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)


        # sets window size and centers it
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        icon = PhotoImage(file="assets/graphics/icon.png")
        root.iconphoto(True, icon)

        #for the bg color when load
        self.root.config(bg=bgcolor)

        self.filename = None  # initialize filename
        self.title = StringVar()  # declare title variable
        self.status = StringVar()  # declare status variable




        self.titlebar = Label(self.root, textvariable=self.title, font=("sans-serif", 10), bd=2, anchor="w", relief=GROOVE)  # creating titlebar
        self.titlebar.pack(side=BOTTOM, fill=BOTH)  # packing titlebar to root window
        self.settitle("Welcome to The Awesome Editor")  # Calling Settitle Function


        # Creating Menubar
        self.menubar = Menu(self.root, font=("sans-serif", 10), activebackground="#aaaaaa")
        # Configuring menubar on root window
        self.root.config(menu=self.menubar)

        # Creating File Menu
        self.filemenu = Menu(self.menubar, font=("sans-serif", 10), activebackground="#aaaaaa", tearoff=0)
        # Adding New file Command
        self.filemenu.add_command(label="New", accelerator="Ctrl+N", command=self.newfile)
        # Adding Open file Command
        self.filemenu.add_command(label="Open", accelerator="Ctrl+O", command=self.openfile)
        # Adding Save File Command
        self.filemenu.add_command(label="Save", accelerator="Ctrl+S", command=self.savefile)
        # Adding Save As file Command
        self.filemenu.add_command(label="Save As", accelerator="Ctrl+A", command=self.saveasfile)
        # Adding Seprator
        self.filemenu.add_separator()
        # Adding Exit window Command
        self.filemenu.add_command(label="Exit", accelerator="Ctrl+E", command=self.exit)
        # Cascading filemenu to menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Creating Edit Menu
        self.editmenu = Menu(self.menubar, font=("sans-serif", 10), activebackground="#aaaaaa", tearoff=0)
        # Adding Cut text Command
        self.editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)
        # Adding Copy text Command
        self.editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)
        # Adding Paste text command
        self.editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)
        # Adding Seprator
        self.editmenu.add_separator()
        # Adding Undo text Command
        self.editmenu.add_command(label="Undo", accelerator="Ctrl+U", command=self.undo)
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        # Creating Help Menu
        self.helpmenu = Menu(self.menubar, font=("sans-serif", 10), activebackground="#aaaaaa", tearoff=0)
        # Adding About Command
        self.helpmenu.add_command(label="About", command=self.infoabout)
        self.helpmenu.add_command(label="License", command=self.licenseread)
        self.helpmenu.add_command(label="Disclaimer", command=self.disclaimer)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Manual", command=self.manual)

        # Cascading helpmenu to menubar
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        # Creating Scrollbar
        scrol_y = Scrollbar(self.root, orient=VERTICAL)

        # creates the text box to edit text
        self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=(configfont, textboxfontsize), state="normal",
                            relief=GROOVE, bg=bgcolor, fg=fgcolor, borderwidth=0)  # cursor="trek"

        # Packing scrollbar to root window
        scrol_y.pack(side=RIGHT, fill=Y)
        # Adding Scrollbar to text area
        scrol_y.config(command=self.txtarea.yview)
        # Packing Text Area to root window
        self.txtarea.pack(fill=BOTH, expand=1)

        # Calling shortcuts funtion
        self.shortcuts()

    # Defining settitle function
    def settitle(self, status):
        # Checking if Filename is not None
        if self.filename:
            # Updating Title as filename
            titlefile = self.filename

        else:
            # Updating Title as Untitled
            titlefile = "Untitled"

        self.title.set(status + " | " + titlefile)
        self.root.title('Awesome Editor v0.0.2' + ' - ' + titlefile)

    # Defining New file Function
    def newfile(self, *args):
        self.txtarea.config(state='normal')
        # Clearing the Text Area
        self.txtarea.delete("1.0", END)
        # Updating filename as None
        self.filename = None
        # Calling settitle funtion
        self.settitle(" ")
        # updating status
        self.settitle("New File Created")

    # Defining Open File Funtion
    def openfile(self, *args):
        self.txtarea.config(state='normal')
        # Exception handling
        try:
            # Asking for file to open
            self.filename = filedialog.askopenfilename(title="Select file", filetypes=(
                ("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))
            # checking if filename not none
            if self.filename:
                # opening file in readmode
                infile = open(self.filename, "r")
                # Clearing text area
                self.txtarea.delete("1.0", END)
                # Inserting data Line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing the file
                infile.close()
                # Calling Set title
                self.settitle(" ")
                # Updating Status
                self.settitle("Opened Successfully")
        except Exception as e:
            messagebox.showerror("Exception", e)

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

    # Defining Cut Funtion
    def cut(self, *args):
        self.txtarea.config(state='normal')
        self.txtarea.event_generate("<<Cut>>")

    # Defining Copy Funtion
    def copy(self, *args):
        self.txtarea.config(state='normal')
        self.txtarea.event_generate("<<Copy>>")

    # Defining Paste Funtion
    def paste(self, *args):
        self.txtarea.config(state='normal')
        self.txtarea.event_generate("<<Paste>>")

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


    def manual(self):
        self.txtarea.config(state='normal')
        # opening file in readmode
        infile = open('assets/texts/manual.txt', "r")
        # Clearing text area
        self.txtarea.delete("1.0", END)
        # Inserting data Line by line into text area
        for line in infile:
            self.txtarea.insert(END, line)

        self.txtarea.config(state='disabled')

        self.title.set('Manual')
        self.root.title('Awesome Editor - Manual')

        self.settitle("Opened Manual")

    def disclaimer(self):
        self.txtarea.config(state='normal')
        # opening file in readmode
        infile = open('assets/texts/disclaimer.txt', "r")
        # Clearing text area
        self.txtarea.delete("1.0", END)
        # Inserting data Line by line into text area
        for line in infile:
            self.txtarea.insert(END, line)

        self.txtarea.config(state='disabled')

        self.title.set('Disclaimer')
        self.root.title('Awesome Editor - Disclaimer')

        self.settitle("Opened Disclaimer")


    # binds key shortcuts
    def shortcuts(self):
        # Binding Ctrl+n to newfile function
        self.txtarea.bind("<Control-n>", self.newfile)
        # Binding Ctrl+o to openfile function
        self.txtarea.bind("<Control-o>", self.openfile)
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
