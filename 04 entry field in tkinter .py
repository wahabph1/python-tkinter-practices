from tkinter import*
root = Tk()
root.title("02 label")
root.geometry("800x800")
root.config(bg="yellow")
lb1= Label(root,text="abdul wahab shaikh", bg="green",fg="blue",font=("times new roman",40,"bold")).pack(fill=X,padx=70)

#entry ek class h jsm hum user s input lete h
lb2= Entry(root, bg="green",fg="yellow",bd=90,relief=GROOVE).pack(fill=X,padx=40,pady=50)
root.mainloop()