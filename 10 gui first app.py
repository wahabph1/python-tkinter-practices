from tkinter import*
root = Tk()
root.title("02 label")
root.geometry("800x700")
root.config(bg="yellow")

def show():
    print("name is ", name.get())
    print("gmail  is ", g.get())
    print("gender is : ",myvar.get())
    print("dept is = ",myvar2.get())
    

myvar =StringVar()
name=StringVar()
g=StringVar()

def show2 ():
   print("dept is = ",myvar2.get())
myvar2 = StringVar()   
lb1 = Label(text="USER ENTRY FORM",bg="pink" ,fg=("blue"),font=("times new roman ",20,"bold"),pady=10 ,relief=GROOVE).pack(fill=X)
use = Label(root,text="USER NAME : ",font="bold",bg="yellow").place(x=350,y=150)
useentry = Entry(root,bg="white",textvariable=name).place(x=500,y=150)
gmail= Label(root,text="GMAIL ACCOUNT : ",font="bold",bg="yellow" ).place(x=350,y=200)
gmailentry = Entry(root,bg="white",textvariable=g).place(x=500,y=203)
gender= Label(root,text="GENDER: ",font="bold",bg="yellow" ).place(x=350,y=260)
male = Radiobutton(root,text="MALE", value="male",bg="yellow", variable=myvar, font="bold").place(x=500,y=255)
feamale = Radiobutton(root,text="FEAMALE",value="feamale", bg="yellow",font="bold" , variable=myvar).place(x=590,y=255)
other = Radiobutton(root,text="OTHER", value="other" ,bg="yellow",font="bold",variable=myvar).place(x=720,y=255)
myvar.set("MALE")

dept= Label(root,text="SELECT DEPT: ",font="bold",bg="yellow" ).place(x=350,y=320)
dept1= Checkbutton(root,text="SOFTWARE ENGINEERING" ,onvalue="software enginnering" , offvalue="nothing" ,variable=myvar2).place(x=500,y=340)
dept2= Checkbutton(root,text="MECHANICAL ENGINNERING", onvalue="mechanical enginnering" , offvalue="nothing",variable=myvar2 ).place(x=500,y=370)
dept3= Checkbutton(root,text="ELECTRICAL ENGINEERING" ,onvalue="electrical engineering" , offvalue="nothing",variable=myvar2).place(x=500,y=400)
dept4= Checkbutton(root,text="CHEMICAL ENGINEERING ",onvalue="chemical engineering" , offvalue="nothing",variable=myvar2).place(x=500,y=430)
dept5= Checkbutton(root,text="TELECOMUNICATION ENGINEERING",onvalue="telecomunication engineering" , offvalue="nothing",variable=myvar2).place(x=500,y=460)
dept6= Checkbutton(root,text="CIVIL ENGINNERING ",onvalue="civil engineering",offvalue="nothing").place(x=500,y=490)
myvar2.set("nothing")
btn = Button(root,text="SUBMIT" , command=show).place(x=500,y=600)





root.mainloop()