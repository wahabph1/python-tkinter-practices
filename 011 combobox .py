from tkinter import*
from tkinter import ttk
root = Tk()
root.geometry("700x400")
root.config(bg="yellow")
def show():
    print(language.get())
language = ttk.Combobox(root,values=("c++","java","html","javascripy","php"),justify=CENTER,state='readonly')
language.place(x=40,y=50,width=250,height=100)
language.set("SELECT A LANGUAGE")
btn= Button(root,text="show", bg ="white",command=show).place(x=0,y=0)
root.mainloop()