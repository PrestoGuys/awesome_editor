# ccp.py
def cut(txtarea):
    txtarea.config(state='normal')
    txtarea.event_generate("<<Cut>>")

def copy(txtarea):
    txtarea.config(state='normal')
    txtarea.event_generate("<<Copy>>")

def paste(txtarea):
    txtarea.config(state='normal')
    txtarea.event_generate("<<Paste>>")
