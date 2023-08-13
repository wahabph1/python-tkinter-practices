from tkinter import*
root = Tk()
root.geometry("700x400")
root.config(bg="yellow")
def show():
 print("your gender is = ",myvar.get())
 

myvar= StringVar()

gender = Label(text="SELECT GENDER : ",bg="yellow").place(x=10,y=20)

male = Radiobutton(root,text="MALE",value="male",variable=myvar).place(x=30,y=40)
feamale = Radiobutton(root,text="FEAMALE",value="feamale",variable=myvar ).place(x=100,y=40)  #yaha variable use hoga ye nh text variable 
myvar.set("MALE")
btm= Button(text="show data" ,command=show).place(x=50,y=150)
root.mainloop()