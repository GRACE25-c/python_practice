#1
student_name="Grace Jacob"
print(student_name,type(student_name))  #Grace Jacob <class 'str'>
age=21
print(age,type(age)) #21 <class 'int'>
height=5.05
print(height,type(height)) #5.05 <class 'float'>
currently_enrolled=True
print(currently_enrolled,type(currently_enrolled))  #True <class 'bool'>
subjects_enrolled=["Maths","History","Physics"]
print(subjects_enrolled,type(subjects_enrolled))  #['Maths', 'History', 'Physics'] <class 'list'>
date_of_birth=(20,"October",2005)
print(date_of_birth,type(date_of_birth)) #(20, 'October', 2005) <class 'tuple'>
skills={ "Java","Flutter","Firebase"}
print(skills,type(skills)) #{'Java', 'Flutter', 'Firebase'} <class 'set'>
Student_details={"name":"Grace","age":21,"course":"PGP"}
print(Student_details,type(Student_details))  #{'name': 'Grace', 'age': 21, 'course': 'PGP'} <class 'dict'>


#2
subject={"python":67,"mathematics":89,"science":39}
total_marks=subject["mathematics"]+subject["python"]+subject["science"]
#print(total_marks)
average=total_marks/len(subject)
#print(average)

if(subject["python"]>=subject["mathematics"]):
    print("highest",subject["python"])
elif(subject["science"]>=subject["mathematics"]):
     print("highest",subject["science"])
elif(subject["python"]>=subject["science"]):
       print("smallest",subject["science"])       #smallest 39
       print("highest",subject["mathematics"])    #highest 89

for subject in subject["mathematics"]>=40, subject["python"]>=40,subject["science"]>=40:
     print(subject)   
#Check whether the student has scored more than 40 in each subject. 
#True
#True
#False


#3

subject={"python":28,"mathematics":33,"science":20}
total_marks=subject["mathematics"]+subject["python"]+subject["science"]
print(total_marks) #81

if(total_marks>=90):
    print("Grace:A")
    print(" the student is eligible for a certificate")
elif(total_marks>=75): #Grace:B
    print("Grace:B")
    print(" the student is eligible for a certificate")
elif(total_marks>=60):
    print("Grace:C")
    print(" the student is eligible for a certificate")
elif(total_marks>=40):
    print("Grace:D")
else:
    print("Grace:F")
for subject in subject["mathematics"]>=12,subject["python"]>=12,subject["science"]>=12:
    print("subjects are Pass",subject)

    
    
#the output will get
#81
#Grace:B
 #the student is eligible for a certificate
#subjects are Pass True
#subjects are Pass True
#subjects are Pass True


#4

marks=[39,55,49,50,58] 
total=marks[0]+marks[1]+marks[2]+marks[3]+marks[4]
for mark in marks:
    print("marks",mark)
print("total marks",total) #251

#output 
# marks 39
# marks 55
# marks 49
# marks 50
# marks 58
# total marks 251


no_of_marks_above40=marks[0]>=40,marks[1]>=40,marks[2]>=40,marks[3]>=40,marks[4]>=40
print(" number of subjects in which the student scored 40 or above: ",no_of_marks_above40.count(True))
print(" number of subjects in which the student scored 40 or below: ",no_of_marks_above40.count(False))

# output
# number of subjects in which the student scored 40 or above:  4
#  number of subjects in which the student scored 40 or below:  1



#5
num=0
while(num<50):
     
     if(num==50):         #displaying 1 to 50 numbers
          print(num)
          num+1
     else:
        num=num+1
     print(num)
print("numbers from 1 to 50")   


num=2
while (num<=50):   #checking even numbers
    print(num)
    num=num+2
print(" these are 1 to 50 even numbers")

num=1
while (num<=50):  #checking odd numbers
    print(num)
    num=num+2
print(" these are 1 to 50 odd numbers")




#6

skills_of_student={"python","flutter","java","java script"}
skills_of_student.add("php")    #add one skill
skills_of_student.remove("java script")  #remove one skill from the set
skills_of_student1={"python"}
print("student knows python",skills_of_student.intersection(skills_of_student1)==skills_of_student1)  #student knows python True
print(skills_of_student)  #{'python', 'java', 'php', 'flutter'}


#7

student={"Student name ":"Grace Jacob","Age":21,"Course":"B.SC Computer Sience","Total marks":6.28,"Grade":"B","Certificate eligibility":"PASS"}
print(student)

#{'Student name ': 'Grace Jacob', 'Age': 21, 'Course': 'B.SC Computer Sience', 'Total marks': 6.28, 'Grade': 'B', 'Certificate eligibility': 'PASS'}