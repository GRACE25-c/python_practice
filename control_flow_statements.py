#***************************************************
#********cONDITIONAL STATEAMENT*********************
#***************************************************



#***********************************************************
#***checking whether the number is bigger than 50***********
#***********************************************************


#number=int(input("enter a number: ")) #get user input and convert the input as number
#number>50 # number>50 # the entterd number is biggger than 50
#number<=50 # the entterd number is equal or lesser than 50
# if(number>50):
#     print("the entterd number is bigger than 50") # intentation

# if(number<50):
#     print("the entterd number is smaller than 50")

# print("end of the program") # just understand the program is end


# if(number>50):
#     print("the entterd number is bigger than 50")

# else:
#     print("the entterd number is smaller than 50")    

# print("end of the program")    
# print("**************************************")
# number=int(input("enter a number: ")) # teack the input from the user
# #reminder = number%2
# if((number%2)==0):
#     print("the given number is even")
# else:
#     print("the given number is odd")
    
# print("*********************************************")   

# temp=float(input("please enter the temperature:  "))
#>=35 : very hot
#25-35 : warm
#15-25 : cold
#<=1 : freezing

# if(temp>=35):
#     print("very hot day")
# else:
#     if(temp>=25):
#         print("warm day")  

#     else:
#         if(temp>=15):
#             print("cold day")
#         else:
#             print("freezing")    

#nexted if else loop


# if(temp>=35):
#     print("very hot day")
# elif(temp>=25):
#     print("warm day")
# elif(temp>=15):
#      print("cold day")
# else:
#     print("freezing")




#print("*************************************************")

#*********************************************
#********iteration steatements****************
#*********************************************

#iteration statements are used when create task  are to be exicuted multiple times
#for loop is used when we know the no. of iteration 

#while_loop is used for when we dont know the no. of  iteration .but condition is know.


#print your name 10 times
# for i in range(10): # we are given the number of iteration

#     print("Grace") #iterative (repitative) task

#print("using step operater")
#for i in range(3,10,3): #we are give the starting and emding iteration using steps operater. 3,4,5,6,7,8,9,10 in this take the step operater we get 3,,6,,9

#for i in range(10,2):# must be the starting point is bigger compaired to end point
 
#range(start,end,step) the step is not enter the step will 1

# for i in range(10,3,-1): #given step as a negative value

#     #starting point should be bigger than the end point. end point is not included in the displaying output .

#     print(i, ' :Grace') #print the no of iteration also/


# print("all odd numbers <50")
# for i in range(1,50,2):
#     print(i)
# print("all odd numbers between 20 to 50")    
# for i in range(21,50,2):
#     print(i)


#********************************************************
#************while loop**********************************
#********************************************************
# print("odd numbers between 50")
# num=1
# while(num <50):
    
#     print(num ,end=",")
#     #num=num+1
#     num=num+2 # use 2 as step operater bacically there is no step operater in the while loop
# #print("end of while loop")

# print("\n""odd numbers between 20 to 50")
# num1=21
# while(num1 <50):
    
#     print(num1, end=",") #end="," is used to cancel the new line print 
#     #num=num+1
#     num1=num1+2 # use 2 as step operater bacically there is no step operater in the while loop
# #print("end of while loop") /


#**********************************************
#********logical operater and control flow statement***********
#***********************************************

age=int(input("enter your age: "))
valid_id=input("do yo have a valid id card (y,n) : ")
if(valid_id=="y"):
    valid_id=True #only if the use enter y
else:
    valid_id=False #only if the use enter n

print("we are checking your eligibility")    

if(age>=18):
    if(valid_id):
        print("you are eligible to vote")
    else:
        print("you are not eligible to vote becouse your age is below 18")  
else:
    print("you are not eligible to vote")         

print("**************************************************")        
if(valid_id and age>=18):
    print("you are eligible to vote ")   

else:
    print("you are not eligible to vote")        