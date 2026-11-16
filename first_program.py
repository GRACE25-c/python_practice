print("hello world!")
print("Whats your name ?")
print("i am grace")
print("were are you from ?")
print("I am from kottayam")
#showing different datatypes 
print('3')#this is a string
print(2026)#this is an intiger
print("2026")#this is also a string
#print('2026") this is a wrong syntax
# we use to comment the entire paragaraph can use ctrl+/ for undo we use the same 

print("type of 2026")
type(2026)
print(type(2026)) #int
print(type(2026.0)) #float
print(type('2026')) #string
print(type("2026")) #string
print('datatype of 2026 is',type(2026)) 
print('datatype of 2026.0 is',type(2026.0)) 
print("datatype of '2026' is",type('2026')) 
print('datatype of "2026" is',type("2026"))
 
print("Datatype of True is",type(True)) #we use to show a boolean datatype then we use first letter will be a capital letter <class 'bool'>
print("datatype of False is", type(False)) #we use to show a boolean datatype then we use first letter will be a capital letter<class 'bool'>

print('*********************************************')
#************************************
#**************Varibles**************
#************************************

my_name = "Grace Jacob"
place_of_birth = "Kottayam"
age = 21
mobile_no = 7306598265
email_id = "gracejacob167@gmail.com"
height = 5.05
print(mobile_no)

fred = 200
john = fred
print(john)

fred = 3
print(john)

#get datatype of a variable

print(type(my_name))
print(type(place_of_birth))
print(type(age))
print(type(mobile_no))
print(type(email_id))
print(type(height))

print('datatype of ',my_name, 'is',type(my_name))
print('datatype of',place_of_birth,'is',type(place_of_birth))
print('datatype of',age,'is',type(age))
print('datatype of',mobile_no,'is',type(mobile_no))
print('datatype of',email_id,'is',type(email_id))
print('datatype of',height,'is',type(height))

print('**********************************************')

#**************************************************
#************data type conversion *****************
#**************************************************

num1=1900 #int
num2= 67.8 #float

print('datatype of ',num1,'is',type(num1)) # this datatype will be int
print('datatype of ',num2,'is',type(num2)) #this datatype will be float

num3 = int(num2) # converted num1 to int
num4= float(num1) #converted num2 into float

print('datatype of ',num3,'is',type(num3))
print('datatype of ',num4,'is',type(num4))