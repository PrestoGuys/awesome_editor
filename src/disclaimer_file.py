# disclaimer_file.py
from tkinter import END

def disclaimer_file(txtarea, title, root, settitle):
    txtarea.config(state='normal')
    # opening file in readmode
    infile = open('assets/texts/disclaimer.txt', "r")
    # Clearing text area
    txtarea.delete("1.0", END)
    # Inserting data Line by line into text area
    for line in infile:
        txtarea.insert(END, line)

    txtarea.config(state='disabled')

    title.set('Disclaimer')

    settitle("Opened Disclaimer")
