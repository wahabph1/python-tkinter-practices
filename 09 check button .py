from tkinter import*
root = Tk()
root.title("02 label")
root.geometry("800x800")
root.config(bg="yellow")
def show():
    print(myvar.get())

myvar=StringVar()
ch1 = Checkbutton(root,text="software anginnering",onvalue="software enginnering" ,offvalue="nothing",variable=myvar).place(x=0,y =10 )
ch2 = Checkbutton(root,text="chemical enginnering",onvalue="chemical enginnering" ,offvalue="nothing",variable=myvar).place(x=0,y =50 )
myvar.set("nothing")

btn = Button(text="show data", command=show).place(x=10,y=100)

root.mainloop()