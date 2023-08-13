from tkinter import*
root= Tk()
from tkinter import  messagebox
root.geometry("700x800")
root.config(bg="black")
mymenu = Menu(root)
def show():
    messagebox.showinfo("About ME",'''ABDUL WAHAB SHAIKH 21SW07
from \nhala new 
country pakistan''')
    
mymenu.add_command(label="About Me",command=show)

newmenu=Menu(mymenu,tearoff=0)
newmenu.add_command(label="21sw07 student" )
newmenu.add_command(label="qurst nawabshah student")
newmenu.add_command(label="from hala new")
mymenu.add_cascade(label="details about me",menu=newmenu)
mymenu.add_separator()
newmenu.add_separator()

newmenu2=Menu(newmenu,tearoff=0)
newmenu.add_cascade(label="gender",menu=newmenu2)
newmenu2.add_command(label="boy")


root.config(menu=mymenu)
root.mainloop()