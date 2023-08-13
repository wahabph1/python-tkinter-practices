from tkinter import*
root= Tk()
root.geometry("700x400")
root.config(bg="yellow")
def show():
  print(lb2.get())
  lb4.config(text=lb2.get()) # get function h jo use hota h enty walw chwez 
  

lb2= Entry(root, bg="green",fg="yellow",bd=15,relief=GROOVE)
lb2.pack(fill=X,padx=40,pady=50) #object banane k lye
lb3= Button(root,text="show me",command=show).place(x=45,y=150)

lb4= Label(root,text="", bg="white",pady=15,fg="yellow",font=("times new roman",10,"bold"))
lb4.place(x=40,y=200)  #object banane k lye

root.mainloop()

