class emp:
   
    i=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
      
    def show(self):
      print("sum of two numbers is " , self.a+self.b) 

    def show2(self):
     print("this is abdul wahab second function for you")

    def show3(self,f,l):
     print("my name is ",f,"my age is ",l) 

       


obj1 = emp(5,6) 
obj2 = emp(9,5)
obj3= emp(4,7)
obj1.show()  
obj2.show()  
obj3.show()  

obj1.show2()  
obj2.show2()  
obj3.show3("abdul wahab" , "20")  
