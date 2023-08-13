from tkinter import*
from tkinter import filedialog
root = Tk()
root.title("02 label")
root.geometry("800x800")
root.config(bg="yellow")

def show ():
    op=filedialog.asksaveasfile()
btn = Button(text="show ",command=show).place(x=0,y=0)
root.mainloop()