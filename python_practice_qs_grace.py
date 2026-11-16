#*******************************************
#***********Identify the Data Type**********
#*******************************************


#1

print("Datatype of 25 is :",type(25))

#2

print("Datatype of 12.5 is :",type(12.5))

#3
print("Datatype of 'Python' is :",type("Python"))

#4
print("Datatype of 'True' is :",type(True))

#5
print("Datatype of 'False' is :",type(False))

#6
print("Datatype of 100 is :",type(100))

#7
print("Datatype of '100' is :",type("100"))

#8
print("Datatype of 3.14 is :",type(3.14))

#9
print('Datatype of "3.14" is :',type("3.14"))

#10
print("Datatype of 0 is :",type(0))


#**************************************************
#**********************True or False***************
#**************************************************

print("****************************************************************")
#11

print("24 is an intiger",(type(25) == int))

#12
print('"25" is a string',(type("25"))==str)

#13
print('12.5 is a float value',type(12.5)==float)

#14
print('"Hello" is a string',type("Hello")==str)

#15
print("True is a booliean value",(type(True)==bool))

#16
print('"True" ia booliean value',(type("True")==bool))

#17
print('"100.0" is an integer',type("100.0")==int)

#18
print("False is a boolean value",type(False)==bool)

#****************************************
#*********Create Variables***************
#****************************************

#19
age=25

#20
name="Grace Jacob"

#21
salary=25000

#22
height=5.8

#23
is_student=True

#24

name="Mary Jacob"
age=54
city="Pala"

#************************************
#**********Predict the Value*********
#************************************

#25
#What will be the value of x?

x=10
x=20
#the value of x is 20

#26
#What will be the value of name?

name="Rahul"
name="Anu"
# the value of name is "Anu"

#27
#What will be the value of x?

x = 10
y = 20
x = y

#  the value of x is 20

#28
#What will be the value of x?

x = 5
x = x + 10
 # the value of x is 15 

 #29
 #What will be the value of marks?

marks = 50
marks = marks + 20
 # the value of marks is 70 

 #***********************Section 3 — Arithmetic Operators **************************

 #30
sum=10+5

#31
subtract=20-8

#32
product=6*5

#33
division=20/4

#34
modules=17%5

#35
floor_division=17//5

#36
squer=2**3

#37
(100 + 50) - 20 

#38

(10 * 5) + 2

#39

(20 / 5 )+ 3

#40

(10 + 5 )* 2 



#**********************************************************************************
#*******************Section 4 — Modulus and Floor Division*************************
#**********************************************************************************

#41

print(15%4)

#42
print(20%3)

#43
print(25%5)


#44
print(17//5)

#45
print(25//4)

#46
print(30//7)

#47
# You have 17 chocolates and want to give 5 chocolates to each student. How many students can receive 5 chocolates? 
total_chocolates=17
want_to_give=5
received_5_chocolates=total_chocolates//want_to_give
print(received_5_chocolates) #3 students will get the 5 chocolates.
# i use floor division operater


#48
print(total_chocolates%5)  # remaining chocolates 2

# modulus operater is used to find the remaining chocolate

#49
#There are 25 students. Each group should contain 4 students. How many complete groups can be formed? 
total_students=25
each_group=4
completed_group=total_students//each_group
print(completed_group) #6 group will be formed

print(total_students%4) #1 student will be left over


#******************************************************
#******************Section 5 — Exponent ***************
#******************************************************


#51
2**2 # the answer is the squer of 2 that is 4

#52
2**3 # the answer is the cube of 2 that is 8

#53
5**2 # the answer is  the squer of 5 that is 25

#54
10**2 # the answer is the squer of 10 that is 100

#55
5**2 # the answer is the squer of 5 that is 25  . we use these **  operater for finding the squer 
5*2 #  the answer is  the product of 5*2 that is 10. we use these *  operater for finding the product of two numbers

#*****************************************************************
#****************Section 6 — Relational Operators*****************
#*****************************************************************

#56

#10>5 this statement is True

#57

#10 < 5 this statement is False

#58

#10 == 10 this statement is True

#59

# 10!=5 this statement is True

#60

#   10 >= 10  this statement is True

#61

#   5 <= 10  this statement is True

#62

#    20 > 20 this statement is False

#63

#   20 >= 20   this statement is True

#64

#  15 != 10 this statement is True

#65

#  5 == 10 this statement is False


#**********************************************************************
#*************Section 7 — Variables + Relational Operators*************
#**********************************************************************

#66
age = 20 # the output of this statement is age is 20 
age > 18 # the output of this statement is age must be  greterthan 18. the out put is true

#67
marks= 45 # the output of this statement is marks is 45
marks==45 # the output of this statement is marks equel to 45

#68

salary = 30000    # the output of this statement is. salary is 30000
salary > 50000    # the output of this statement is. salary lessthan 50000. the out is false

#69

temperature = 35  # the output of this statement is. temperature is 35
temperature >= 30 # the output of this statement is. temperature is greaterthan or equlto 35


#70

password = "python"   # the output of this statement is. password is python
password == "Python"  # the output of this statement is. password is equal to python

#71

x = 10 # x is 10 
y = 20 # y is 20
x < y  # x lessthan y  thats mean 10<20 the output will be true

#72

x = 10  # x is 10
y = 20  # y is 20
x == y # x==y its mean 10==20 .false


#*******************************************************
#*************Section 8 — Strings***********************
#*******************************************************


print("*****************************************")

#73
name="Python"

#74

name[0]  #first character of: name = "Python". that is p

#75

name[-1] #the last character. that is n

#76

name[2] # 2 nd index chatrecter is t

#77

name[4] # 4 th index chatrecter is o

#78

name = "Python" 
print(name[0]) 
#the output of this steatment is p

#79

name = "Python" 
print(name[1]) #the output of this steatment is y



#80

name = "Python" 
print(name[-1]) #the output of this steatment is n


#**********************************************************
#*************Section 9 — String Slicing*******************
#**********************************************************

#81

word = "Python" 
print(word[0:2]) #the output of this steatment is "py"

#82

word = "Python" 
print(word[0:3]) #the output of this steatment is "pyt"

#83

word = "Python" 
print(word[2:5]) #the output of this steatment is "tho"


#84

word = "Python" 
print(word[:3]) #the output of this steatment is "Pyt"

#85

word = "Python" 
print(word[3:]) #the output of this steatment is "hon"

#86

word = "Python"
print(word[0:3])#the output of this steatment is "pyt"

#87
word = "Python"
print(word[3:7]) #the output of this steatment is "hon"

#88
word = "Python" 
print(word[1:4])

#******************************************************
#**************Section 10 — String Methods ************
#******************************************************

#89
name = "python" 
print(name.upper()) #the output is PYTHON

#90
name = "PYTHON" 
print(name.lower())  #the output is python

#91
name = "python" 
print(name.capitalize()) #the output is Python

#92
converted= "hello world"
print(converted.upper()) #the output is HELLO WORLD

#93
second_convertion="PYTHON PROGRAMMING"
print(second_convertion.lower()) #the output is python programming

#94
print(name.capitalize()) #the output is python

#95
 
# difference between: 
#upper() this function is used for change into capital letters
#lower() this function is used for change into small letters

#96

name = "pYtHoN" 
print(name.upper()) #the output is PYTHON

#97
name = "pYtHoN" 
print(name.lower()) #the output is python

#*********************************************
#**********Section 11 — \n and \t*************
#*********************************************

#98
print("Hello \nWorld")

#99
print("Name\tAge")

#100

#print("Hello\nWorld") the output is Hello
# #world

#101

#print("Name\tAge") the out put is Name    Age

#102
print("Python\nIs easy")

#103
print("Name\tRahul\nAge\t20\nCity\tKochi")

#***************************************************
#***********Section 12 — Mixed Questions************
#***************************************************

#104
a=10
b=5

sum=a+b # the output will be 15
difference=a-b # the output will be 5
product=a*b # the output will be 50
division=a/b # the output will be 2

#105

marks=75
marks>50 # True

#106
age=18
age>=18 # True

#107

number=25
az=number%5
print(az==0) #the number is divisible by 5. True

#108

number = 17
number%3 # the output is 2

#109
name = "Python" 
print(name[0])
print(name[-1])
print(name[0:3])
print(name.upper())
print(name.lower())

#110

price = 100   
quantity = 5 
total_price= price*quantity

#111
maths = 80 
science = 75 
english = 90 
total_marks= maths + science + english # 245 total marks


#112
price_of_per_pen=10
total_pen=7
total_cost=price_of_per_pen + total_pen # 70 total cost

#113

total_amount=500
i_spend=275
in_my_hand=total_amount-i_spend


#114
total1_student=27
group_have=5
completed1_group=total1_student//group_have #5 grouops


#115
# how many students are left after creating the complete groups

left_over=total1_student%5


#****************************************************
#*******Section 13 — Small Real-Life Problems********
#****************************************************

#116
age=21
age>=18 

#117
marks=65
marks>=40

#118
shirt_price=800
trousers_cost=1200
total_cost=shirt_price+trousers_cost

#119
#You have ₹500. You spend ₹199 on a recharge. How much money is left?
money_have=500
spend_recharge=199
money_left=money_have-spend_recharge

#120
chocolates=32
students=6
#1
each_student_get=chocolates//students #5 chocolates
#2
remain=chocolates%6 # 2 chocolates remain
#print(remain)

#121
a = 25 
b = 40
a>b #False
a<b #True
a==b #False
a!=b #False

#122

pen=2
per_pen=20
notbooks=3
per_notbooks=50
total_bill=(2*20)+(3*50)


#123
salary=25000
bonus=3000
new_salary=salary+bonus


#124

name = "programming"
print(name[0]) #p
print(name[1]) #r
print(name[-1])#g
print(name[0:4])#pro
print(name[-1:-4])#gni
print(name.upper())#PROGRAMMING
print(name.lower())#programming
print(name.capitalize())#Programming

#125
Name="Rahul"
Age=25
City="Kochi"
Salary=30000

print("Name:\t",Name)
print("Age:\t",Age)
print("City:\t",City)
print("Salary:\t",Salary)
