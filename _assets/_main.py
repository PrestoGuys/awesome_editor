# Awesome Editor v0.0.1 - July 16, 2024 
# Made by PrestoGuys in 2024
# this is the main python file for awesome editor

import tkinter as tk
import toml
from tkinter import ttk
from tkinter import * 

def main():
	# opens the config file and saves it in a variable 
	with open('CONFIG/main.toml', 'r') as f:
		configtoml = toml.load(f)


	# gets theme from config file
	configtheme = configtoml['Settings']['Theme']

	if configtheme == 'dark':
		bgcolor = '#333333'

	if configtheme == 'light':
		bgcolor = '#fdfdfd'


	if configtheme == 'dark':
		fgcolor = '#fdfdfd'

	if configtheme == 'light':
		fgcolor = '#141414'


	root = Tk()


	resolution = 720 # pixels

	tempres = resolution * 1.3333333333333333333333333333333333333333 # 40 threes, just in case
	window_width  = round(tempres)
	window_height = resolution

	print(tempres)
	print(window_width)

	# gets screen_width and screen_height
	screen_width  = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()

	# gets senter of the screen
	center_x = int(screen_width/2 - window_width / 2)
	center_y = int(screen_height/2 - window_height / 2)

	# sets window size and centers it
	root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

	# This is the section of code which creates the main window
	root.configure(background='#393939')
	root.title('Awesome Editor - ')


	root.mainloop()