from tkinter import*
r = Tk()
r.title("abd")
r.geometry("800x400")
r.resizable(False,False)
r.config(bg= "yellow")
# lbl=Label(r,text="abdul wahab shaikh").grid(row=0,column=0)
# lbl2=Label(r,text="fazul din shiakh from hala new" ,bg="green").grid(row=2,column=8) # grid me yahe problem h hum nh kaer skte define thek se jagah widgets ke




#Labl3= Label(r,text="i am a pack ").pack() # by default ism at ah center p
#labl4 = Label(r,text="this is second labele ").pack(side=LEFT)
#labl5 = Label(r,text="this is second labele ").pack(fill=X)
#labl6 = Label(r,text="this is second labele ").pack(fill=X)
#labl7 = Label(r,text="this is second labele ").pack(fill=X)
#labl8= Label(r,text="this is second labele ").pack(expand=1, fill=BOTH) # fill ye use hota h pore expamd krne k lye 
lab= Label(r,text="abdul wahab").place(x=200,y=20)
lab= Label(r,text="abdul wahab").place(x=200,y=20)
lab= Label(r,text="abdul wahab").place(x=50,y=50)
r.mainloop()