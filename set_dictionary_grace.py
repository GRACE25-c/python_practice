#1
fruits={"Apple" , "Banana" ,"Orange" , "Mango" , "Grapes" }
print(fruits)
print("number of fruits",len(fruits))


#2
numbers = [10, 20, 10, 30, 20, 40, 50, 30]  #[] this is a list
numbers1={10, 20, 10, 30, 20, 40, 50, 30}  #{} this is a set
numbers1.remove(10) #{50, 20, 40, 30}
print(numbers1)


#3
colors={"red", "blue", "green"} 
colors.add("yellow") 
colors.add("black")
colors.remove("blue")
print(colors) #{'green', 'yellow', 'red', 'black'}


#4
student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"} 
both_sub=student1.intersection(student2) 
print(both_sub) #{'Python', 'SQL'}



#5
print("all subjects studied by either student",student1.union(student2)) #print(" subjects studied only by Student 1.",student1)
print(" subjects studied only by Student 1.",student1) #subjects studied only by Student 1. {'HTML', 'Java', 'SQL', 'Python'}
print(" subjects studied only by Student 2.",student2)  #subjects studied only by Student 2. {'CSS', 'C++', 'SQL', 'Python'}

#6
student={"name":"Rahul","age":20,"course":"Python","city":"Kochi"}
print("the complete dictionary:",student)
# print(type(student))
print(student["name"]) #feaching some this from the set like this . #Rahul
print(student["age"])   #20
print(student["course"]) #Python

#7
employee = {"name": "Anu", "age":25,"salary":25000,"department":"IT"}
employee["salary"]=30000 #{'name': 'Anu', 'age': 25, 'salary': 30000, 'department': 'IT'}
employee["age"]=26
print(employee)


#8
marks = {"Maths": 80, "Science":75 , "English":90, "Computer": 85}
print(marks.keys()) #dict_keys(['Maths', 'Science', 'English', 'Computer'])
print(marks.values()) #dict_values([80, 75, 90, 85])
total_marks=marks["Computer"]+marks["English"]+marks["Maths"]+marks["Science"]
number_of_items=len(marks)
print("the total marks is: ",total_marks)
print("the average marks: ",total_marks/number_of_items)


#9
student = {"name": "Arun",    "marks": 85 ,"English": 90,  "age": 21, "course": "Python" }
print(type(student))
print("student name is ",student["name"],".","course studying ",student["course"])

student["Grade"]="A" # THIS STEP INCLUDE THE KEYS IN "GRADE"
student["Grade"]="A" # WE GET THE KEY AS GRADE AND JEST DO " student["Grade"]="A""" THIS STEP ONES MORE
if(student["marks"]>=50):
 print("Pass") 
else:
 print("Fail")
for i in student.items():
 print(i)
# print(student)



#10

morning_batch = {"Anu", "Rahul", "Arun", "Meera"} 
evening_batch = {"Rahul", "Meera", "John", "Priya"}

intersect_batch=morning_batch.intersection(evening_batch)
print("Students who attend both batches",intersect_batch) #{'Meera', 'Rahul'}
#nion=morning_batch.union(evening_batch)
ntersect_batch=morning_batch.difference(evening_batch)


print("Students who attend only the morning batch:",ntersect_batch) #Students who attend only the morning batch: {'Arun', 'Anu'}
intersect1_batch=evening_batch.difference(morning_batch)
print("Students who attend only the evening batch:",intersect1_batch) #Students who attend only the evening batch: {'John', 'Priya'}
print("All unique student names across both batches:",ntersect_batch.union(intersect1_batch)) #All unique student names across both batches: {'Arun', 'Priya', 'Anu', 'John'}

