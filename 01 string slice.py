# about string and its indexes : 

a = "Abdul wahab" # length is sixe-1 always


# print(type(a))    # function h ye type janine k lye 
# # a[4]= g  this is will not work hum string m chage nh kar skte
# # concating two strings means sum of two strings
# # negative index bhi hote h isme  or wo 0 se nh -1 s start hoga 
# print(a[0]) # character at index 0 will so where   


# # slicing 
# print(a[0:3])  # iska matlab h ye 0 se 2 index tak print karo isko he kahte h slice slice matlab tukre karna
# print(a[0:])  # ye pore 0 se last tak krega 0:4
# print(a[:4])  # ye 0 se 3 index tak krega print :  
# print("after",a[:]) # ye bhi full krega print
# print("Ff",a[-4:-1])  # same as a[1:4] '''

# # skipping characters in string :

# print("string after skiping is ",a[0::3])  # iska matlab  2 character skip karke phr print karo char 
# print("string after skiping is ",a[0::2])  # iska matlab  1 character skip karke phr print karo char 

# string funcions 
#print("length of string is  == ",len(a))
#print("this string ending with the word b is it true or not this functions returns boolean value : ",a.endswith("b"),"yes it exist ")
#print("characters with the name of a size is =  ",a.count("a"))
#print(a.capitalize()) # first word ko capatalize krega just
#print("replacing string abdul wahab to ",a.replace("wahab","basit"))
#print(a.find("wahab")) # find krega ye word wahab kis index s start ho raha or character bhi d skte h hum isme:
#print(a.endswith("b")) # ye boolean value return karega kya humare string b word se end ho rahe h ye nahi yaha p word bhi d skte  h hum


# escape sequence :
# /n /t /' // 