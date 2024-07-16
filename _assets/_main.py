# Awesome Editor v0.0.1 - July 16, 2024 
# Made by PrestoGuys in 2024
# this is the main file of code for awesome editor

import tkinter as tk
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



	# This is the section of code which creates the main window
	root.geometry('640x480')
	root.configure(background='#393939')
	root.title('Awesome Editor - ')

	root.mainloop()