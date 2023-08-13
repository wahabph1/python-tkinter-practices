from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("900x800")
root.config(bg="black")
def message1():
    messagebox.showinfo("show info","you id is working now")

def message2 ():
    messagebox.showwarning("error message","wrong acccount")
    
def message3():
    messagebox.showerror("error","something is wrong here")    
btn1= Button(text="messagw 1" ,command=message1).place(x=4,y=5)
btn2= Button(text="messagw 2" ,command=message2 ).place(x=100,y=5)
btn3= Button(text="messagw 3" ,command=message3 ).place(x=300,y=5)
root.mainloop()