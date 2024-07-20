	root = Tk()


	resolution = 720 # pixels, 4:3 aspect ratio

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