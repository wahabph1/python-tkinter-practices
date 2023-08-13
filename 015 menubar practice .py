from tkinter import*
root= Tk()
from tkinter import  messagebox
root.geometry("700x800")
root.config(bg="black")
menu1 = Menu(root)
file = Menu(menu1)
format = Menu(menu1)
view = Menu(menu1)
root.config(menu=menu1)

# menu bar code 
menu1.add_cascade(label="File" , menu=file)
menu1.add_command(label="Edit")
menu1.add_cascade(label="Formit",menu=format)
menu1.add_cascade(label="view",menu=view)
menu1.add_command(label="Help")

# file menu code
file.add_command(label="New                                       Ctrl+N  ")
file.add_command(label="New Window                       Ctrl+Shift+N  ")
file.add_command(label="Open...                                  Ctrl+O ")
file.add_command(label="Save                                      Ctrl+S  ")
file.add_command(label="Save As...                             Ctrl+Shift+N  ")
file.add_separator()
file.add_command(label="Page Setup...                     ")
file.add_command(label="Print...                                  Ctrl+P ")
file.add_separator()
file.add_command(label="Exit                ")


# format code
format.add_command(label="Word wrap")
format.add_command(label="Font...")


# view code

view.add_command(label="Zoom")
view.add_command(label="Status Bar")




root.mainloop()