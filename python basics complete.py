# print ("abdul wahab")
# name = "abdul wahab shaikh "
# age = 20
# print ("my name is = "+ name + "my age is =  "+str(age))

#typecasting : most important concept in python 
# age = input("what is your age")
# age = int(age)
# if age >10 :
#     print("you are adult")
# else:
#     print("you are child")

# calculator
# num1 = input("enter first number ")
# op = input("enter operator +-*/")
# num2 = input("enter second number ")

# num1 = int(num1)
# num2= int(num2)
# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op =="/":    
#     # print(num1//num2) ye is lye h hum nh chahte float m ans ae humara :
#     print(num1/num2)
# else :
#     print("invalid")

# i=10
# while i>=1:

#      print(i * "*")
#      i= i-1 # ism c++ k tarah ye nh h i++; 

# for item in range (1):
#
#    print(item+100)

# i=0
# for item in 
#     print("hello")
#     i=i+3

# logical operators
# print(3>2 or 3==3)
# print(3>2 and 3==3)
# print(3>2  not 3==3)

# comparison operator
# print(3!=2)

# print(3==3)
# print(3>3)
# print(3<5)


# list data type :
# collection of items 
# marks = [20, 40 ,50 ,500]  # bake languages me positive index hote h per python
#me enegative bhi h -3 mtlb peche se start ho 
# print(marks[-3])
# print(marks[0:2]) # hum ye use krte h hum kitne index tak values chye 2 include nh index

# marks.clear()  to clear whole list
# print(marks)


# i=0
# while i<len(marks):
#      print("printing numbers at index " +str(i ), marks[i])
#      i = i+1  
# marks.append(5555)
# marks.insert(0,100)
# print(100 in marks)
# for score in marks:
#     print(score)
# num = len(marks) # function for length to know list
# print(num)


#tuple  tuble list ke tarah hota h par bus isme koe operation apply nh kar skte jese
# delete insert update

#  marks =(100,400,400)
# marks[0]= 4  ye error deta h chnage nh kar skte hum

marks =(100,400,400,400,400,400)
print(marks.count(400))  # ye function hume ye batata h 400 kitne bar h humare tuple me  
print(marks.index(400))  # ye function ye batata 400 ka pahela index kya h

# set unique elements no repition allow
marks ={100,400,400,400,400,400,"abdul wahab"} #syntax of set
# list  []  
# tuple () tuple me ye zarori mh h()
# set {}

print(marks) # dekho isme 400 ek bar he atraha h repition wale nu,bers ignore kar rahe
# set me index nh hote isko hum ye nh kar skte print (marks[0]) index s access nh kar skte
# set ko unordered kahte h
# jinhe index ho order kahte h 
#print k lye  
# for dis in marks:
#     print(dis)


# dictionary  isme key pairs ate h values mtlb ke index se nh ksi name se
marks = {"name" : "abdul wahab shaikh 0" , "age": " 20"}
print(marks["name"] , marks["age"]) # yaha dekho hum yaha p koe index nh use kar rshe
#usk key value se access kar rahe...

# insertion
# marks["city"]= "hala";   ye age kahe b jagah add kar rahe
# print(marks["city"])


# #updation 
# marks["name"]= "abdul basit shaik"
# print(marks["name"])



# functions
# 1 in built function int(), str()
# 2 module function realted functions and related variables combine make the module
# example import math
# import math
# print(dir(math)) # to show all functions 
# from math import sqrt 
# from math import *      # sub math k functions module
# print(sqrt(int(4)))
# 3 user define function

# user define functio

def fun():
    print("hello this is abdul wahab ")
    
fun()

def sum (a,b):
    print("Sum is ", a+b , "by by")

sum(1,4)    
    


