from tkinter import*
root = Tk()
root.geometry("900x800")
root.config(bg="black")

def show(price_):
    lbl.config(text=str(price.get()))
    print(str(price.get()))
price= Scale(root,from_=1, to=500,length=700,sliderlength=200,orient=HORIZONTAL,command=show,showvalue=False)
price.place(x=20,y=40)


lbl= Label(root,bg="yellow")
lbl.place(x=0,y=0,width=500,relwidth=1)

root.mainloop()