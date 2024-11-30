from tkinter import END

def manual(txtarea, title, root, settitle):
    txtarea.config(state='normal')
    # opening file in readmode
    infile = open('assets/texts/manual.txt', "r")
    # Clearing text area
    txtarea.delete("1.0", END)
    # Inserting data Line by line into text area
    for line in infile:
        txtarea.insert(END, line)

    txtarea.config(state='disabled')

    title.set('Manual')
    root.title('Awesome Editor - Manual')

    settitle("Opened Manual")
