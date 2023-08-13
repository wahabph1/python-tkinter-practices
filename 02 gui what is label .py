from tkinter import*
root = Tk()
root.title("02 label")
root.geometry("800x800")
root.config(bg="yellow")
# lable ek class h python m jese tk class h usk ander or different classes h wese he label he 
#or label use kya jata h text and images lagane k lye 
lb1= Label(root,text="abdul wahab shaikh", bg="green",fg="blue",font=("times new roman",40,"bold")).pack(fill=X,padx=70)
lb2= Label(root,text="abdul wahab shaikh", bg="white",fg="yellow",font=("times new roman",40,"bold")).pack(fill=X,pady=20)
lb3= Label(root,text="abdul wahab shaikh", bg="white",fg="yellow",font=("times new roman",40,"bold")).pack(fill=X,pady=20,padx=40)
lb4= Label(root,text="abdul wahab shaikh", bg="white",pady=40,fg="yellow",font=("times new roman",40,"bold")).pack(fill=X,pady=20,padx=10)

lb5= Label(root,text="abdul wahab shaikh", relief=RAISED, bg="white",pady=40,fg="yellow",font=("bold")).pack(fill=X,pady=20,padx=10)
lb6= Label(root,text="abdul wahab shaikh", relief=SUNKEN, bg="white",pady=40,fg="yellow",font=("bold")).place(x=40,y=30,height=40,width=400)
lb6= Label(root,text="abdul wahab shaikh", relief=GROOVE, bg="white",pady=40,fg="yellow",font=("bold")).pack(fill=X,pady=20,padx=10)







root.mainloop()