# #1
# student_list=["Grace","Mary","Jacob","Shalomi","George"]
# print(student_list) #the output will get ['Grace', 'Mary', 'Jacob', 'Shalomi', 'George']
# name=input("enter your name: ")
# student_list.append(name) #add the user enterd name into the student_list
# print(student_list) #the  output ['Grace', 'Mary', 'Jacob', 'Shalomi', 'George', 'Nice']

# #2

# list1 = ["Rice", "Sugar", "Milk"] 
# list2 = ["Bread", "Eggs", "Butter"] 
# list1.extend(list2)
# print(list1)
# print("the number of iteams in the list:",len(list1))


# #3
# numbers = [10, 20, 10, 30, 40, 10, 20, 50] 
# print(numbers)
# enter_number=int(input("enter a number from the list: "))
# print(numbers.count(enter_number)) # enter a number from the list: 50.  the out put will i get 1



# #4

# natural_numbers_list=[1,2,3,4,5,6,7,8,9,10]
# print(natural_numbers_list)
# natural_numbers_list.reverse()
# print("reversed list",natural_numbers_list) 

# #5
# marks =[78, 45, 92, 56, 88, 34, 67] 
# marks.sort()
# print("the sorted list is : ",marks) #the sorted list is :  [34, 45, 56, 67, 78, 88, 92]
# marks.reverse()
# print("the decending order list is : ",marks)  #the decending order list is :  [92, 88, 78, 67, 56, 45, 34]

# #6

# fruits = ["Apple", "Banana", "Mango", "Orange"]
# fruits_list=input("enter a fruits name: ")
# fruits_list_position=int(input(" enter the position where the fruit should be added: "))
# fruits.insert(fruits_list_position,fruits_list) 
# print(fruits) #['Apple', 'Banana', 'Mango', 'kiwi', 'Orange']

# #7

# subjects = ["English", "Maths", "Science", "Computer", "History"]
# print(" the original list is","\n",subjects) #history
# print(subjects.pop())
# print("the updated list is ",'\n',subjects)

# #8

# colours = ["Red", "Blue", "Green", "Yellow", "Blue"] 
# print(colours) #['Red', 'Blue', 'Green', 'Yellow', 'Blue']
# color1=(input("enter a colour you want to remove: ")).capitalize()
# colours.remove(color1)
# print(colours) #['Red', 'Blue', 'Green', 'Blue']


# #9
# programming_languages=["C","Cpp","Python","Java","Java Script"]
# print("this is the orginal list: ",programming_languages) #this is the orginal list:  ['C', 'Cpp', 'Python', 'Java', 'Java Script']
# programming_languages.clear()
# print("this is the updated list: ",programming_languages) #this is the updated list:  []

# #10

# students = ["Anu", "Rahul", "Meera", "Arun","Diya"]
# students.append("Kiran") 
# print("Add a new student named 'Kiran'","\n",students)
# print("\n")
# students2=["Sneha","Vijay"]
# students.extend(students2)
# print("Add two more students","\n",students)
# print("\n")
# students.insert(2, "Ravi")
# print("Insert 'Ravi' at the second position","\n",students)
# print("\n")
# #students.count("anu")
# count=students.count("Anu")
# print(' how many times "Anu" appears: ',count)
# #print("Count how many times 'Anu' appears","\n",students)
# print("\n")
# students.sort()
# print(" the student names alphabetically","\n",students)
# print("\n")
# students.remove("Rahul")
# print('Remove "Rahul"',"\n",students)
# print("\n")
# students.pop()
# print('Remove the last student',"\n",students)
# print("\n")
# students.reverse()
# print("the  final attendance list is :","\n",students)


