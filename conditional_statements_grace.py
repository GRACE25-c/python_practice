#1
number=int(input("enter a number: "))
if(number>=0):
 print("the entered number is positive")

else:
 print("the entered number is negative")

 #2
 age=int(input("enter the age: "))
 if(age>=18):
  print("you are  are eligible to vote")
 else:
  print("you are not eligible")  

  #3
  number=int(input("enter an integer: "))
  if(number%2==0):
   print("the number is even")
  else:
   print("the number is odd")

   #4
   password="grace123"
   password1=input("enter a password: ")
   if(password==password1):
    print("Access Granted")
   else:
    print("Access Denied")

    #5
number1=int(input("enter first number : "))
number2=int(input(" enter second number : "))
if(number1>number2): # which one is greater
 print("greater number is",number1)
else:
 print("greater number is",number2)

 if(number1==number2):
  print("both numbers are equal")
 else:
  print("not equal")

#6
marks=int(input("enter your marks out of 100 : "))
if(marks<=100 & marks>=90):
 print("your Grade is A")
elif(marks<=89 & marks>=80):
 print("your Grade is B")
elif(marks<=79 & marks>=70):
 print("your Grade is C")
elif(marks<=69 & marks>=60):
 print("your Grade is D")
elif(marks<=59 & marks>=50):
 print("your Grade is E")
elif(marks<=49 & marks>=1):
 print("your Grade is F")
else:   # if the entered marks are below 0 or above 100 that will be the invalid value
 print("Invalid Marks")

 #7
# teak input from the user
num1=int(input("enter fist number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if(num1<=num2): #check the second number is largest
 print("largest",num2)
elif(num1>=num3):  #check the first number is largest
 print("largest",num1)
else:  #check the third number is largest
 print("largest",num3)

#8
color=input("enter a traffic light colour: ").capitalize() #user enter input . i given this ".capitalize()" used to capitalice the input from the user 
Red="Stop"
Yellow="Get Ready"
Green="Go"
Any_other_input="Invalid Signal"

if color=="Red":
 print(Red)

elif(color=="Yellow"):
 print(Yellow)

elif(color=="Green"):
 print(Green)

else:
 print(Any_other_input)



10

account_balance=10000
withdrawal_amount=int(input("enter the withdrawal amount: ")) #Ask the user to enter the withdrawal amount
#Check whether the amount is positive.
if(withdrawal_amount>=0):
 print("the amount is positive")
#Check whether the withdrawal amount is a multiple of 100.
multiple_of_100 = (withdrawal_amount//100)
print(multiple_of_100)

#sufficient_balance=account_balance - withdrawal_amount
if(account_balance - withdrawal_amount!=0):
 print("sufficient balance is available")

remaining=(account_balance - withdrawal_amount)
print("remaining balance is ",remaining)

#9
# first_100_units=100*2
# next_100_units=100*3
#next_100_units1=100*5
above_300_units=300*7

unit=int(input("enter the consumer unit: "))
if(unit<=100):
 print("Total Bill=",unit*2)
elif(unit<=200):
 print("Total Bill=",100*2+(unit-100)*3)
elif(unit<=300):
 print("Total Bill=",100*2 + 100*3 + (unit - 200)*5)
elif(unit<=above_300_units):
 print("total Bill=",100*2 + 100*3 + 100*5 + (unit-300)*7)