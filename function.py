#function to add two numbers

def display_sum(num1,num2):  #function input
    sum=num1+num2
    print("sum of ",num1,'and',num2 ,"is",sum)
#     #a fuction will have 
#     # 1.function name 
#     #2. inputs(s)
#     #3. body of the function (what the fuction actually does)
#     #(4).output.
#     # why we define inpout  variables in the function definition , we are creating new variables with scope within the function.
# display_sum(8,7)    # function calling or invoking the function   the out is 'sum of  8 and 7 is 15'
# display_sum(2026,8)
# display_sum(9.8,6.6)           
                  # sum of  8 and 7 is 15
                  # sum of  2026 and 8 is 2034
                  # sum of  9.8 and 6.6 is 16.4

def display_sum_custom():
    print("we will display the sum of two numbers")
    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))
    sum=num1+num2
    print("sum of ",num1,'and',num2 ,"is",sum)
# display_sum_custom()
# # we will display the sum of two numbers
# # enter first number: 16.5
# # enter second number: 7.6
# # sum of  16.5 and 7.6 is 24.1

def display_name():
    name=input("enter your name: ")
    print("Hi",name)
    print("Good afternoon")
    print("How are you?")

#display_name()    

# # **************************get a multiplication table ****************************************


# num=5
# print("multiplication table of",num)
# for i in range(1,11):
#     print(i,"*",num,"=",i*num)

# num=8
# print("multiplication table of",num)
# for i in range(1,11):
#  print(i,"*",num,"=",i*num) 

# #   function to display a multiplication table of any number

def multiplication_table():
   print("multiplication table of your enterd number")
   num=int(input("enter a number : "))
   print("multiplication table of",num)
   for i in range(1,11):   #how many time iterate
    #print(i,"*",num,"=",i*num) 
    print(f"{i} x {num} = {i*num}") 


#multiplication_table()  #invoking the function

def subject():
#score_sub1=int(input("enter your first subject score: "))  
#  score_sub2=int(input("enter your second subject score: "))
#  score_sub3=int(input("enter your third subject score: "))
#  score_sub4=int(input("enter your forth subject score: "))
#  score_sub5=int(input("enter your first subject score: "))
#  sum=score_sub1+score_sub2+score_sub3+score_sub4+score_sub5
    tuple1=(40,75,66,74,66)
    #print( tuple1)
    
    if tuple1[0]>=tuple1[1]:
       print("largest",tuple1[0])
    elif tuple1[2]>=tuple1[3]:
             print("largest",tuple1[2])  
    else:
         print("largest",tuple1[4]) 


    if tuple1[0]<=tuple1[1]:
           print("smallest",tuple1[0])
    elif tuple1[2]<=tuple1[3]:
                 print("smallest",tuple1[2])  
    else:
             print("smallest",tuple1[4])    
def subject_sum():
    tuple1=(40,75,66,74,66)
    sum=tuple1[0]+tuple1[1]+tuple1[2]+tuple1[3]+tuple1[4]
    print("total marks",sum)

def subject_average():  
    tuple1=(40,75,66,74,66) 
    length=len(tuple1) 
    sum=tuple1[0]+tuple1[1]+tuple1[2]+tuple1[3]+tuple1[4]
    avarege=sum/length             
    print("avereage marks",avarege)

# subject()
# subject_sum()
# subject_average()


# def calculate_sum(tuple1):
#     sum=0
#     for i in range(len(tuple1)):
#         sum=sum+tuple1[i]
#     print(f'total score = {sum}')  
#     return sum
      


# def calculate_avg(tuple1):
#      total= calculate_sum(tuple1)
#      count=len(tuple1)
#      average=total/count
#      print(f'average score = {average}')
#      return average


# score_sub1=int(input("enter your first subject score: "))  
# score_sub2=int(input("enter your second subject score: "))
# score_sub3=int(input("enter your third subject score: "))
# score_sub4=int(input("enter your forth subject score: "))
# score_sub5=int(input("enter your fifth subject score: "))

# tuple1=(score_sub1,score_sub2,score_sub3,score_sub4,score_sub5)

# #avg = calculate_avg(tuple1)





#****************************************************************************
#**********************optional arguments************************************
#*****************************************************************************


def calculate_exponent(num,exp=2):   #num,exp=2 function arguments
     print(num**exp)

# calculate_exponent(5)  #25
# calculate_exponent(5,3)   #125



# hear wish is an optional iinput. default value here is good morning
def create_wish(name,wish="good morning"):
     print(f'Hi {name},{wish}')
create_wish("grace")
create_wish("grace","you are so butiful")

#pre difind functions are built in function like print(),while() etc.

#we can give values of arguments explicitly
create_wish(wish="how are you",name="Grace")


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




