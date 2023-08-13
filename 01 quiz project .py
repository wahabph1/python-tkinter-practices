from tkinter import ttk
from tkinter import*
import random
import time
import datetime
from tkinter import messagebox
root = Tk()
root.title("02 label")
root.geometry("1540x800+0+0")
root.title("hospital")
root.config(bg="black")

lti = Label(root,text="HOSPITAL MANAGEMENT SYSTEM",font=("aria",50,"bold"),bd=20,fg="red",bg="white",relief=RIDGE)
lti.pack(side=TOP,fill=X)










##functionality#################




def name():
    name= pname.get()
    fathername= fname.get()
    disease= dname.get()
    contact= coname.get()
    city=cityname.get()
    country= countryname.get()
    adress=adressname.get()
    admit=doaname.get()
    discharge= dodname.get()
    birthday= dobname.get()
    bp=bpname.get()
    dibities= dibiname.get()
    blood=bgname.get()
    patientid= pidname.get()
    relation = relaname.get()
    occupation= occuname.get()
    medicine= mediname.get()
    
    
    print("PATIENT NAME  = ",name,"\nFATHER NAME",fathername,"\nDisease = ",disease,"\ncity =",city,"\nCountry = ",country,"\nContact",contact,"\nAdress",adress,"\nDate of Admit",admit,"\nDate of Dicharge ",discharge,"\nDate of birthday",birthday,"\nBlood pressure",bp,"\nDiabities",dibities,"\nBlood Group",blood,"\nPatient id ",patientid,"\nRelation Status",relation,"\nOccupation",occupation,"\nmedicine",medicine)
  
  
    
    
    
    
    
    
pname = StringVar()  
    
fname = StringVar()  
    
cname = StringVar()  
    
dname = StringVar()  
    
coname = StringVar()  
    
cityname = StringVar()  
    
countryname = StringVar()  
    
adressname = StringVar() 

doaname = StringVar() 

dodname = StringVar() 


dobname = StringVar() 


surname = StringVar()  

bpname = StringVar()  

dibiname = StringVar()  

bgname = StringVar()  
    

pidname = StringVar()  


relaname = StringVar()  
    

occuname = StringVar()  


mediname = StringVar()  
    
        
    
    
    
     
     
     
     

   












 ################################data frames ##################
 
Dataframe =Frame(root,bd=20,relief=RIDGE)
Dataframe.place(x=0,y=120,width=1530,height=400)

dataframeleft = LabelFrame(Dataframe ,bd=20,padx=20,relief=RIDGE ,bg="light salmon" ,fg="Blue",text="Patient Details",font=("aria",12,"bold"))
dataframeleft.place(x=0,y=5,width=900,height=350)


dataframeRight = LabelFrame(Dataframe ,bd=20,padx=20,relief=RIDGE , fg="Blue", font=("aria",12,"bold"), text="Prescription")
dataframeRight.place(x=900,y=5,width=400,height=350)


################# button frames ############

btnlabel= Frame(root,bd=20,relief=RIDGE)
btnlabel.place(x=0,y=600,width=1500,height=70)


#######################left frame data############################


lblname= Label(dataframeleft,text="Patient Name :", bg="light salmon",font=("aria",12,"bold") ,padx=2,pady=6 )
lblname.grid(column=0,row=0,sticky=W)


lblnameenter= Entry(dataframeleft,bg="LightBlue1", textvariable=pname , bd=4,width=35)
lblnameenter.grid(column=1,row=0,sticky=W)


lblfather= Label(dataframeleft,text="Father Name:",bg="light salmon" , font=("aria",12,"bold") ,padx=2,pady=6 )
lblfather.grid(column=0,row=1,sticky=W)


lblfatherenter= Entry(dataframeleft,bg="LightBlue1", textvariable=fname, bd=4,width=35)
lblfatherenter.grid(column=1,row=1,sticky=W)


lblc= Label(dataframeleft,text="Contact Number:", font=("aria",12,"bold") ,bg="light salmon" ,padx=2,pady=6 )
lblc.grid(column=0,row=2,sticky=W)

lblcenter= Entry(dataframeleft,bg="LightBlue1", textvariable=cname, bd=4,width=35)
lblcenter.grid(column=1,row=2,sticky=W)


lblcity= Label(dataframeleft,text="City:",  font=("aria",12,"bold") ,bg="light salmon" ,padx=2,pady=6 )
lblcity.grid(column=0,row=3,sticky=W)

lblcityenter= Entry(dataframeleft,bg="LightBlue1",textvariable=cityname, bd=4,width=35)
lblcityenter.grid(column=1,row=3,sticky=W)



lblcountry= Label(dataframeleft,text="Coutry:", font=("aria",12,"bold") ,bg="light salmon" ,padx=2,pady=6 )
lblcountry.grid(column=0,row=4,sticky=W)

lblcountryenter= Entry(dataframeleft,bg="LightBlue1", textvariable=countryname,  bd=4,width=35)
lblcountryenter.grid(column=1,row=4,sticky=W)





lbldisease= Label(dataframeleft,text="Disease Name:", font=("aria",12,"bold"),bg="light salmon"  ,padx=2,pady=6 )
lbldisease.grid(column=0,row=5,sticky=W)

lbldiseaseenter= Entry(dataframeleft,bg="LightBlue1", textvariable=dname, bd=4,width=35)
lbldiseaseenter.grid(column=1,row=5,sticky=W)





lblDateofadmint= Label(dataframeleft,text="Date of Admint:", font=("aria",12,"bold"),bg="light salmon"  ,padx=2,pady=6 )
lblDateofadmint.grid(column=0,row=6,sticky=W)

lbldateenter= Entry(dataframeleft,bg="LightBlue1", textvariable=doaname, bd=4,width=35)
lbldateenter.grid(column=1,row=6,sticky=W)



lblDateofdischarge= Label(dataframeleft,text="Date of Discharge:", font=("aria",12,"bold"),bg="light salmon"  ,padx=2,pady=6 )
lblDateofdischarge.grid(column=0,row=7,sticky=W)

lbldischargerenter= Entry(dataframeleft,bg="LightBlue1", textvariable=dodname, bd=4,width=35)
lbldischargerenter.grid(column=1,row=7,sticky=W)





lbldateofbirthday= Label(dataframeleft,text="Date of bithday:", font=("aria",12,"bold") ,bg="light salmon" ,padx=2,pady=6 )
lbldateofbirthday.grid(column=0,row=8,sticky=W)


lbldischargerenter= Entry(dataframeleft,bg="LightBlue1",textvariable=dobname, bd=4,width=35)
lbldischargerenter.grid(column=1,row=8,sticky=W)




### secod size

lbls= Label(dataframeleft,text="Surname:", font=("aria",12,"bold") ,bg="light salmon" ,padx=50,pady=6)
lbls.grid(column=2,row=0,sticky=W)


lblsurnameenter= Entry(dataframeleft,bg="LightBlue1", textvariable=surname,  bd=4,width=35)
lblsurnameenter.grid(column=3,row=0,sticky=W)



lblblodd= Label(dataframeleft,text="Blood pressure:", font=("aria",12,"bold"),bg="light salmon"  ,padx=50,pady=6 )
lblblodd.grid(column=2,row=1,sticky=W)


lblbloodenter= Entry(dataframeleft,bg="LightBlue1", textvariable=bpname, bd=4,width=35)
lblbloodenter.grid(column=3,row=1,sticky=W)




lblmedi= Label(dataframeleft,text="MEDICATION:", font=("aria",12,"bold") ,bg="light salmon" ,padx=50,pady=6 )
lblmedi.grid(column=2,row=2,sticky=W)



lblmedicationenter= Entry(dataframeleft,bg="LightBlue1",  textvariable=mediname, bd=4,width=35)
lblmedicationenter.grid(column=3,row=2,sticky=W)


lblptid= Label(dataframeleft,text="Patient ID:", font=("aria",12,"bold"),bg="light salmon"  ,padx=50,pady=6 )
lblptid.grid(column=2,row=3,sticky=W)


lblptenter= Entry(dataframeleft,bg="LightBlue1", textvariable=pidname, bd=4,width=35)
lblptenter.grid(column=3,row=3,sticky=W)


lbldia= Label(dataframeleft,text="Diabities:", font=("aria",12,"bold"),bg="light salmon"  ,padx=50,pady=6 )
lbldia.grid(column=2,row=4,sticky=W)


lbldiaenter= Entry(dataframeleft,bg="LightBlue1", textvariable=dibiname, bd=4,width=35)
lbldiaenter.grid(column=3,row=4,sticky=W)



lblgroup= Label(dataframeleft,text="Blood group:", font=("aria",12,"bold"),bg="light salmon"  ,padx=50,pady=6 )
lblgroup.grid(column=2,row=5,sticky=W)



lblbloodenter= Entry(dataframeleft,bg="LightBlue1", textvariable=bgname, bd=4,width=35)
lblbloodenter.grid(column=3,row=5,sticky=W)



lblrela= Label(dataframeleft,text="Relation Status:", font=("aria",12,"bold"),bg="light salmon"  ,padx=50,pady=6 )
lblrela.grid(column=2,row=6,sticky=W)


lblrelationenter= Entry(dataframeleft,bg="LightBlue1", textvariable=relaname, bd=4,width=35)
lblrelationenter.grid(column=3,row=6,sticky=W)



lbloccu= Label(dataframeleft,text="Occupation:", font=("aria",12,"bold") ,bg="light salmon" ,padx=50,pady=6 )
lbloccu.grid(column=2,row=7,sticky=W)

occupation= Entry(dataframeleft,bg="LightBlue1", textvariable=occuname, bd=4,width=35)
occupation.grid(column=3,row=7,sticky=W)






######## Buton######3
bntexit= Button(btnlabel,text="Submit",width=140 ,font=("aria",12,"bold"),bg="sky blue1",command=name)
bntexit.grid(row=0,column=6)



























root.mainloop()