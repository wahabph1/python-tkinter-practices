from tkinter import*
root = Tk()
root.title("02 label")
root.geometry("800x800")
root.config(bg="yellow")

def show():
    print(myvar.get())
    #labl.config(text=text.get())
    labl.config(text=myvar.get())
    
myvar = StringVar()    

#text = Entry(bg="white")
#text.place(x=10,y=20,width=500)

text = Entry(bg="white",textvariable=myvar).place(x=10,y=20,width=500,height=600)
but= Button(text="show me ",command=show).place(x=10,y=40)
labl= Label(text="",bg="yellow")
labl.place(x=0,y=500,relwidth=1)


root.mainloop()