from tkinter import*
root=Tk()
root.geometry("800x800")
root.config(bg="yellow")
def show():
    print(feed.get("1.0",END))
    lbl.config(text=feed.get("1.0",END))
btn= Button(text="show" ,command=show).place(x=10,y=10)
lbl = Label(text="",bg="white")
lbl.place(x=120,y=15)
feed = Text(root)
feed.place(x=40,y=50)


root.mainloop()