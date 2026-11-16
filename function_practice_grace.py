#1

def calculate_grade():

    student_marks=int(input("enter your marks: "))
    
    if student_marks>=90:
        print("A")
    elif student_marks>=75:
        print("B")
    elif student_marks>=60:
        print("C")
    elif student_marks>=40:
        print("D")
    else:
        print("Fail")  

#calculate_grade()

#2

def calculator():
    number1=int(input("enter first number: "))
    number2=int(input("enter first number: "))
    operator1=input("enter any operator +, -, *, /  :  ")
    if (operator1 == "+"):
        print(number1 + number2)
    elif (operator1 == "-"):
        print(number1 - number2)
    elif (operator1 == "*"):
            print(number1 * number2)
    elif (operator1 == "/"):
            print(number1 / number2)
    else:
        print("invalide operator")        
    return calculator
#calculator()    

#3

def simple_interest():
    principal=int(input("enter your total amount: ")) #enter your total amount: 10000
    rate=int(input("enter interest rate: ")) #enter interest rate: 5
    time=int(input("how many months: ")) #how many months: 9
    interest=(principal * rate * time )/100
    print("interest",interest)  #interest 4500.0
    return interest

#simple_interest()


#4

def last_character():
    words=input("type anything you like:  ")
    word=words[-1]
    #print("last character is ",word)
    return word
#last_char=last_character()
#print("The last character of the string",last_char)

#5
def calculate_bill():
    electricity_units=int(input("enter your electricity units consumed: "))
    first=100*5
    next=100*7
    above=200*10
    if electricity_units>=first:
        bill=first+( electricity_units - first)*5
        print("total amount",bill)
    elif  electricity_units>=next:
        bill=first+ next+ ( electricity_units -next)*7
        print("total amount",bill)
    
    elif  electricity_units>=above:
            bill=first+ next+above+ ( electricity_units -above)*10
            print("total amount",bill)


#calculate_bill()
#output
# enter your electricity units consumed: 670
# total amount 1350

#6

def count_even():
    print("this will display numbers upto the user entered numbers")
    num1=int(input("enter a numbers: "))
    list1=[]
    print("even numbers")
    count=0
  
    for num1 in range(1,num1):
        if num1%2==0:
            #list1.insert(num1,num1)
            #count=count+1 
            print(num1)
            #list1.insert(num1,num1)
            #print(list1) 
            
            print(count)  
#count_even()      



#******************************************************************
#******************************************************************
#******************************************************************

def divide(num,den):
     result=num/den
     print(f"the answer is {result}")
# divide(40,5)     
# divide(1234,678)
# divide("a","b")  #TypeError: unsupported operand type(s) for /: 'str' and 'str'
# divide(1234,0)   #ZeroDivisionError: division by zero


#*******************************************************
#exception handling.
# we write specific criteria so that code flow is not interrupted.
# we write a potential running error making code inside "try" block
# # and the exception  with be caght by the "except block"

#rewriting the fuction with exception block
def divide_new(num,den):
     try:
        result=num/den
        print(f"the answer is {result}")
     except:
          print("there is a problem")
     print("you reach the end of the function")

# divide_new(40,5) 
# divide_new("a","b")      
# divide_new(1234,678)

# divide_new(1234,0) 
# divide_new(55,5) 


#************************************************************************************************************************************

#rewrite the function with exception block displaying the error message
def divide_new1(num,den):
     try:
        result=num/den
        print(f"the answer is {result}")
     except Exception as e:
          print(f"there is a problem: {e}")
     

# divide_new1(40,5) 
# divide_new1("a","b")      
# divide_new1(1234,678)

# divide_new1(1234,0) 
# divide_new1(55,5) 

#output
# the answer is 8.0
# # there is a problem: unsupported operand type(s) for /: 'str' and 'str
# # the answer is 1.8200589970501475
# # there is a problem: division by zero
# # the answer is 11.0


#******************************************************************************************************************

#rewrite the function with exception block displaying the appropriate error message
def divide_new2(num,den):
     try:
        result=num/den
        print(f"the answer is {result}")
     except TypeError:
          print("please mack suar your enterd numbers")
     except ZeroDivisionError:
          print("please mack suar your enterd numbers is a non zero value as denominater")
     except Exception as e:
        print(f"ther is a problem: {e}")   
     print("the end")  

divide_new2(40,5) 
divide_new2("a","b")      
divide_new2(1234,678)

# divide_new2(1234,0) 
# divide_new2(55,5)
