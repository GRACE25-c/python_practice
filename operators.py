#*****************************************
#**********Ariyhmatics********************
#*****************************************

# binary operations : we need a min of two operands.

num1=389
num2=5

sum=num1 + num2 #addition
difference=num1 - num2 #subtraction
product=num1 * num2 #multiplication
division=num1 / num2 
exponent=num1 ** num2
reminder=num1 % num2
floor=num1 // num2

print("sum of thes two numbers",num1, '+', num2 ,'=',sum)
print("difference of thes two numbers",num1, '-', num2 ,'=',difference)
print("product of thes two numbers",num1, '*', num2 ,'=',product)
print("division of thes two numbers",num1, '/', num2 ,'=',division)
print("exponent of thes two numbers",num1, '**', num2 ,'=',exponent)
print("reminder of thes two numbers",num1, '%', num2 ,'=',reminder)
print("floor divition of thes two numbers",num1, '//', num2 ,'=',floor)


#********************************************************
#*******************condisional operators****************
#********************************************************
print("******************************************************************************************************")

#num1=389
#num2=5

print(num1,'>', num2, num1>num2)
print(num1,'<', num2, num1<num2)
print(num1,'>=', num2, num1>=num2)
print(num1,'<=', num2, num1<=num2)
print(num1,'==', num2, num1==num2)
print(num1,'!=', num2, num1!=num2)


#********************************************
#************Logical operators***************
#********************************************

print("******************************************************************************************")

#AND - All has to be in the aggriment
#OR  - at least one condision must be in aggriment
#NOT - Opposite



#operands will be boolean

statement_1= True
statement_2= False
statement_3= True
statement_4= False

#AND

print(statement_1 and statement_2) #True and False = False
print(statement_1 and statement_3)#True and True = True
print(statement_1 and statement_4)#True and False = False

#OR

print(statement_1 or statement_2) #True or False = True
print(statement_1 or statement_3) #True or true = True
print(statement_2 or statement_4) #False and False = False

#NOT

print(not statement_1) #False
print(not statement_2) #True

