# frame kya hoat h frame sub window hota h ek window me ek s zydh window hona:
from tkinter import*
root= Tk()
from tkinter import  messagebox
root.geometry("1400x800")
window1 = Frame(root,bd=10,bg="green",relief=GROOVE)
window1.place(x=20,y=40,width=350,height=400)
lbl= Label(window1,text="abdul wagha s").place(x=40,y=50)
btn = Button(window1,text="show").place(x=40,y=100)


window2 = LabelFrame(root,bd=10,bg="green",relief=GROOVE)
window2.place(x=400,y=40,width=350,height=400)
lbl= Label(window2,text="frame lebel").place(x=40,y=50)   # faeda y h koi bhi button ya kch bhi hum banana chae isme bana skte h hum

root.mainloop()