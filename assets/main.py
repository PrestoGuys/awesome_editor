# Awesome Editor v0.0.1 - July 16, 2024
# Made by PrestoGuys in 2024
# This is the main python file for The Awesome Editor.

# Credit to www.codespeedy.com for some starter code.
# Link: https://www.codespeedy.com/create-a-text-editor-in-python/

# Importing Required Libraries

# Awesome Editor v0.0.1
# Made By PrestoGuys in 2024
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
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import toml

# Inporting Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


# links to the text editor class?
def main():
	TextEditor


class TextEditor:
	def __init__(self, root):
		print('''
Awesome Editor v0.0.1
Made By PrestoGuys in 2024
==========================

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

=====================================================================
(From License)

	15. Disclaimer of Warranty.

	THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

	16. Limitation of Liability.

	IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.
''')

		# opens the config file and saves it in a variable 
		with open('CONFIG/main.toml', 'r') as f:
			configtoml = toml.load(f)


		configtheme     = configtoml['Settings']['Theme']            # gets theme
		configfont      = configtoml['Settings']['Editor_Font']      # gets editor font
		textboxfontsize = configtoml['Settings']['Editor_Font_Size'] # gets editor font size


		# sets background color from cofig file
		if configtheme == 'dark':
			bgcolor = '#333333'

		if configtheme == 'light':
			bgcolor = '#fdfdfd'


		# sets foreground color from cofig file
		if configtheme == 'dark':
			fgcolor = '#fdfdfd'

		if configtheme == 'light':
			fgcolor = '#141414'


		# prints the config gile settings
		print('Config: ')
		print(configtheme)
		print(configfont)
		print('')
		print(bgcolor)
		print(fgcolor)


		# assigns root
		self.root = root

		
		# window width and window height of the program
		window_width  = 1100
		window_height = 750


		# gets screen_width and screen_height
		screen_width  = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()


		# gets senter of the screen
		center_x = int(screen_width/2 - window_width / 2)
		center_y = int(screen_height/2 - window_height / 2)


		print(window_width)  # prints window width
		print(window_height) # prints window height
		print('')
		print(screen_width)  # prints screen width
		print(screen_height) # prints screen height
		print('')
		print(center_x)      # prints center of the screen x coord
		print(center_y)      # prints center of the screen y coord


		# sets window size and centers it
		self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


		icon = PhotoImage(file="assets/graphics/icon.png")
		root.iconphoto(True,icon)


		#for the bg color when load
		self.root.config(bg=bgcolor)


		self.filename = None        # initialize filename
		self.title    = StringVar() # declare title variable
		self.status   = StringVar() # declare status variable


		self.titlebar = Label(self.root,textvariable=self.title,font=(configfont,15),bd=2,relief=GROOVE) # creating titlebar
		self.titlebar.pack(side=TOP,fill=BOTH) # packing titlebar to root window
		self.settitle() # Calling Settitle Function


		# Creating Statusbar
		self.statusbar = Label(self.root,textvariable=self.status,font=(configfont,15),bd=2,relief=GROOVE)
		# Packing status bar to root window
		self.statusbar.pack(side=BOTTOM,fill=BOTH)
		# Initializing Status
		self.status.set("Welcome to Awesome Editor")

		# Creating Menubar
		self.menubar = Menu(self.root,font=(configfont,15),activebackground="#990000")
		# Configuring menubar on root window
		self.root.config(menu=self.menubar)


		# Creating File Menu
		self.filemenu = Menu(self.menubar,font=(configfont,12),activebackground="#990000",tearoff=0)
		# Adding New file Command
		self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
		# Adding Open file Command
		self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
		# Adding Save File Command
		self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
		# Adding Save As file Command
		self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
		# Adding Seprator
		self.filemenu.add_separator()
		# Adding Exit window Command
		self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
		# Cascading filemenu to menubar
		self.menubar.add_cascade(label="File", menu=self.filemenu)


		# Creating Edit Menu
		self.editmenu = Menu(self.menubar,font=(configfont,12),activebackground="#990000",tearoff=0)
		# Adding Cut text Command
		self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
		# Adding Copy text Command
		self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
		# Adding Paste text command
		self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
		# Adding Seprator
		self.editmenu.add_separator()
		# Adding Undo text Command
		self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
		# Cascading editmenu to menubar
		self.menubar.add_cascade(label="Edit",menu=self.editmenu)


		# Creating Help Menu
		self.helpmenu = Menu(self.menubar,font=(configfont,12),activebackground="#990000",tearoff=0)
		# Adding About Command
		self.helpmenu.add_command(label="About",command=self.infoabout)

		self.helpmenu.add_command(label="README",command=self.indepthabout)
		self.helpmenu.add_command(label="License",command=self.licenseread)

		# Cascading helpmenu to menubar
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)


		# Creating Scrollbar
		scrol_y = Scrollbar(self.root,orient=VERTICAL)
		
		# creates the text box to edit text
		self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=(configfont, textboxfontsize), state="normal", relief=GROOVE, bg=bgcolor, fg=fgcolor, borderwidth=0) # cursor="trek"
		
		# Packing scrollbar to root window
		scrol_y.pack(side=RIGHT,fill=Y)
		# Adding Scrollbar to text area
		scrol_y.config(command=self.txtarea.yview)
		# Packing Text Area to root window
		self.txtarea.pack(fill=BOTH,expand=1)


		# Calling shortcuts funtion
		self.shortcuts()

	# Defining settitle function
	def settitle(self):
		# Checking if Filename is not None
		if self.filename:
			# Updating Title as filename
			titlefile = self.filename

		else:
			# Updating Title as Untitled
			titlefile = "Untitled"

		print(titlefile)

		self.title.set(titlefile)
		self.root.title('Awesome Editor' + ' - ' + titlefile)

	# Defining New file Function
	def newfile(self,*args):
		self.txtarea.config(state='normal')
		# Clearing the Text Area
		self.txtarea.delete("1.0",END)
		# Updating filename as None
		self.filename = None
		# Calling settitle funtion
		self.settitle()
		# updating status
		self.status.set("New File Created")

	# Defining Open File Funtion
	def openfile(self,*args):
		self.txtarea.config(state='normal')
		# Exception handling
		try:
			# Asking for file to open
			self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
			# checking if filename not none
			if self.filename:
				# opening file in readmode
				infile = open(self.filename,"r")
				# Clearing text area
				self.txtarea.delete("1.0",END)
				# Inserting data Line by line into text area
				for line in infile:
					self.txtarea.insert(END,line)
				# Closing the file	
				infile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Opened Successfully")
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining Save File Funtion
	def savefile(self,*args):
		self.txtarea.config(state='normal')
		# Exception handling
		try:
			# checking if filename not none
			if self.filename:
				# Reading the data from text area
				data = self.txtarea.get("1.0",END)
				# opening File in write mode
				outfile = open(self.filename,"w")
				# Writing Data into file
				outfile.write(data)
				# Closing File
				outfile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Saved Successfully")
			else:
				self.saveasfile()
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining Save As File Funtion
	def saveasfile(self,*args):
		self.txtarea.config(state='normal')
		# Exception handling
		try:
			# Asking for file name and type to save
			untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
			# Reading the data from text area
			data = self.txtarea.get("1.0",END)
			# opening File in write mode
			outfile = open(untitledfile,"w")
			# Writing Data into file
			outfile.write(data)
			# Closing File
			outfile.close()
			# Updating filename as Untitled
			self.filename = untitledfile
			# Calling Set title
			self.settitle()
			# Updating Status
			self.status.set("Saved Successfully")
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining Exit Funtion
	def exit(self,*args):
		op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
		if op>0:
			self.root.destroy()
		else:
			return

	# Defining Cut Funtion
	def cut(self,*args):
		self.txtarea.config(state='normal')
		self.txtarea.event_generate("<<Cut>>")

	# Defining Copy Funtion
	def copy(self,*args):
		self.txtarea.config(state='normal')
		self.txtarea.event_generate("<<Copy>>")

	# Defining Paste Funtion
	def paste(self,*args):
		self.txtarea.config(state='normal')
		self.txtarea.event_generate("<<Paste>>")

	# Defining Undo Funtion
	def undo(self,*args):
		self.txtarea.config(state='normal')
		# Exception handling
		try:
			# checking if filename not none
			if self.filename:
				# Clearing Text Area
				self.txtarea.delete("1.0",END)
				# opening File in read mode
				infile = open(self.filename,"r")
				# Inserting data Line by line into text area
				for line in infile:
					self.txtarea.insert(END,line)
				# Closing File
				infile.close()
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Undone Successfully")
			else:
				# Clearing Text Area
				self.txtarea.delete("1.0",END)
				# Updating filename as None
				self.filename = None
				# Calling Set title
				self.settitle()
				# Updating Status
				self.status.set("Undone Successfully")
		except Exception as e:
			messagebox.showerror("Exception",e)

	# Defining About Funtion
	def infoabout(self):
		messagebox.showinfo("About Awesome Editor","Awesome Editor\nv0.0.1 - BETA\nMade By PrestoGuys in 2024\nLicense: https://www.gnu.org/licenses/gpl-3.0.txt")


	def indepthabout(self):
		self.txtarea.config(state='normal')
		# opening file in readmode
		infile = open('extra/texts/README_MESSAGE.txt',"r")
		# Clearing text area
		self.txtarea.delete("1.0",END)
		# Inserting data Line by line into text area
		for line in infile:
			self.txtarea.insert(END,line)

		self.txtarea.config(state='disabled')

		self.title.set('README')
		self.root.title('Awesome Editor - README')

		self.status.set("Opened README")

	def licenseread(self):
		self.txtarea.config(state='normal')
		# opening file in readmode
		infile = open('extra/texts/LICENSE.txt',"r")
		# Clearing text area
		self.txtarea.delete("1.0",END)
		# Inserting data Line by line into text area
		for line in infile:
			self.txtarea.insert(END,line)

		self.txtarea.config(state='disabled')
		
		self.title.set('License')
		self.root.title('Awesome Editor - License')

		self.status.set("Opened GNU GPL 3 License")

	# binds key shortcuts
	def shortcuts(self):
		# Binding Ctrl+n to newfile funtion
		self.txtarea.bind("<Control-n>",self.newfile)
		# Binding Ctrl+o to openfile funtion
		self.txtarea.bind("<Control-o>",self.openfile)
		# Binding Ctrl+s to savefile funtion
		self.txtarea.bind("<Control-s>",self.savefile)
		# Binding Ctrl+a to saveasfile funtion
		self.txtarea.bind("<Control-a>",self.saveasfile)
		# Binding Ctrl+e to exit funtion
		self.txtarea.bind("<Control-q>",self.exit)

		# sets cut, copy, and paste
		self.txtarea.bind("<Control-x>",self.cut)
		self.txtarea.bind("<Control-c>",self.copy)
		self.txtarea.bind("<Control-v>",self.paste)

		self.txtarea.bind("<Control-u>",self.undo)

root = Tk() # creating TK container
TextEditor(root) # passing root to text editor class
root.mainloop() # root window loop