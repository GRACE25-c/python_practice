# ##1
# num=int(input("enter a number :  "))
# if num>0:
#     print("the number is positive : ",num)
# else:
#     print("the number is negative: ",num)

# ##2

# age=int(input("enter your age : "))
# if age>=18:
#     print("you are eligible for voting: ")
# else:
#     print("you are not eligible for voting")

# ##3

# num=int(input("enter an intiger: "))
# if num%2==0:
#     print("the number is even:",num)
# else:
#     print("the number is odd: ",num)

# ##4

# password="grace@123"
# passw=input("enter your password: ")
# if passw==password:
#     print("Access Granted")
# else: 
#     print( "Access Denied" )


# ##5

# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# if num1<num2:
#     print(f"{num2} is greatest")
# elif num1>num2:
#     print(f"{num1} is greatest")
# elif num2<num1:
#     print(f"{num2} is smallest")
# elif num1<num2:
#     print(f"{num1} is smallest")
   
# else:
#     print("both are equal")


# ##6

# mark=int(input("enter your total marks out of 100: "))
# if 100<mark:
#     print("invalid marks")
# elif mark>=90:
#     print("A")
# elif mark>=80:
#     print("B")
# elif mark>=70:
#     print("C")
# elif mark>=60:
#     print("D")
# elif mark>=50:
#     print("E")
# else:
#     print("Faill")


### 7

# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))
# num3=int(input("enter third number: "))

# if num1>num2:
#     print(f"{num1} is largest")
# elif num3>num2:
#     print(f"{num3} is largest")
# else:
#     print(f"{num2} is largest")

    

###8

# color=input("enter a color from this Red,Yellow,Green: ").capitalize()
# if color=="Red":
#     print("Stop")
# elif color=="Yellow":
#     print("Get Ready")
# elif color=="Green":
#     print("Go")
# else:
#     print("Invalid Signal")   


##9


# unit=int(input("enter your consumes units : "))
# first=100*2
# next=100*3
# next1=100*5
# above=300*7

# if 100>=unit:
    
#     print("your total bill is : ",unit*2)
# elif 200>=unit:
    
#     print("your total bill is : ",first+(unit-100)*3)
# elif 300>=unit:
    
#     print("your total bill is : ",first+next+(unit-200)*5)
# elif above>=unit:
    
#     print("your total bill is : ",first+next+next1+(unit-300)*7)
       

# ##10

# balance=10000
# withdraw=int(input("enter your withdrawal amount: "))
# sufficient=balance-withdraw
# if withdraw>=0:
#     print("the mount is not positive ")
# if withdraw%100==0:
#     print("whether the withdrawal amount is a multiple of 100 ")
# else:
#     print(" the withdrawal amount is not a multiple of 100. ")
# if sufficient<=0:
#     print("the balance is zero")
# else:
#     print("sufficient balance is ",sufficient)



###########################################################################################

##1
# student_name=["grace","nice","mary","shalomi","jacob"]
# print(student_name)
# student_name.append("george") #add some thing into list we use append
# print(student_name)


##2
# list1 = ["Rice", "Sugar", "Milk"] 
# list2 = ["Bread", "Eggs", "Butter"]
# list1.extend (list2)
# print(list1)
# # list3=list1.count()
# # print(list3)
# print(len(list1))  #number of items len()

# ##3
# numbers = [10, 20, 10, 30, 40, 10, 20, 50]
# num=int(input("enter a number: "))

# print(numbers.count(num))

# ##4

# list1=[1,2,3,4,5,6,7,8,9,10]
# list1.reverse()
# print(list1)

# ##5

# marks = [78, 45, 92, 56, 88, 34, 67]
# marks.sort()
# print(marks)
# marks.reverse()
# print(marks)

# ##6
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# fruit_name=input("enter any fruite name: ")
# fruit_position=int(input("enter the position where the fruit should be added the position start from 0 : "))
# fruits.insert(fruit_position,fruit_name)
# print(fruits)

# ##7

# subjects = ["English", "Maths", "Science", "Computer", "History"]
# print(subjects)

# print(subjects[-1])
# subjects.pop()
# print(subjects)

# ##8

# colours = ["Red", "Blue", "Green", "Yellow", "Blue"]
# remove=input("enter a color you want to remove frome this Red, Blue, Green, Yellow, Blue:  ").capitalize()
# colours.remove(remove)
# print(colours)

# ##9

# programing=["python","cpp","c","java","dart"]
# print(programing)
# programing.clear()
# print(programing)

###10

# students = ["Anu", "Rahul", "Meera", "Arun", "Diya"]

# students.append("kiran")
# list3=["sneha","vijay"]
# students.extend(list3)
# students.insert(2,"ravi")
# print(students.count("Anu"))
# students.sort()
# students.remove("Rahul")
# students.pop()
# students.reverse()
# print(students)

##############################################################################
###1
# fruits={"Apple","Banana","Orange","Mango","Grapes"}
# print(fruits)
# print(len(fruits))


##2

#numbers = [10, 20, 10, 30, 20, 40, 50, 30] 
# numbers={10, 20, 10, 30, 20, 40, 50, 30}
# print(numbers)


# ##3

# colors={"red", "blue", "green"}
# colors.add("yellow")
# colors.add("black")
# colors.remove("blue")
# print(colors)


# ##4

# student1 = {"Python", "Java", "SQL", "HTML"} 
# student2 = {"Python", "C++", "SQL", "CSS"}
#print("both students are studying ",student1.intersection(student2))


# ##5
# print(" all subjects studied by either student ",student1.union(student2))
# print(" subjects studied only by Student 1 ",(student1).difference(student1.intersection(student2)))
# print("subjects studied only by Student 2 ",(student2).difference(student1.intersection(student2)))


# ##6

# student={"name":"Rahul","age":"20","cource":"python","city":"kochi"}
# print(student)
# print(student.get("name"))
# print(student.get("age"))
# print(student.get("cource"))

# ##7
# employee = { "name": "Anu", "age": 25,"salary": 25000}
# employee["department"]="IT"
# employee["department"]="IT"
# employee["salary"]=30000
# employee["age"]=26
# print(employee)


# ##8
# marks = { "Maths": 80,"Science": 75,"English": 90,"Computer": 85}
# print(marks.keys())
# print(marks.values())
# print(marks["Computer"]+marks["English"]+marks["Maths"]+marks["Science"])
# print((marks["Computer"]+marks["English"]+marks["Maths"]+marks["Science"])/len(marks))

##9


student = {"name": "Arun","marks": 85,"English": 90,"age": 21,"course": "Python"}

print(student["name"])
print(student["age"])
if (student["marks"]>=50):
    print("the student has scored 50 or above ")
    print("Pass")
else:
    print(" the student has scored below 50")
    print("Fail")
student["grade"]="A"
student["grade"]="A"
for keys,values in student.items():
    print(keys ,":" ,values)