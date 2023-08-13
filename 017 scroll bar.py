from tkinter import*
root = Tk()
root.title("02 label")
root.geometry("800x800")
fra= Frame(root)
fra.place(x=40,y=30,width=400,height=400)

data = Listbox(fra,justify=CENTER)
data.place(x=0,y=0,relheight=1,relwidth=1)

for i in range(1,400):
   data.insert(i," data is      "+ str(i))
   
   






root.config(bg="yellow")
root.mainloop()