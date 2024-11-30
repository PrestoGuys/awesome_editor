# open_file.py
from tkinter import messagebox, filedialog, END

def openfile(txtarea, settitle):
    txtarea.config(state='normal')

    try:
        # Asking for file to open
        filename = filedialog.askopenfilename(title="Select file", filetypes=(
            ("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py")))

        if filename:
            infile = open(filename, "r")  # Opening chosen file in readmode
            txtarea.delete("1.0", END)  # Clearing the text area

            for line in infile:
                txtarea.insert(END, line)  # Inserting data Line by line into text area

            infile.close()  # Closing the file

            settitle(" ")  # Calling settitle
            settitle("Opened Successfully")  # Updating settitle

    except Exception as e:
        messagebox.showerror("Exception", e)
