#**********************************************************************************************
#*****************python fundamentals using define function************************************
#**********************************************************************************************




#1
def student_details():
     
     name=input("enter student name: ")
     age=int(input("enter student age: "))
     height=float(input("enter student height: "))
     currently_enrolled=bool(input("currently enrolled: "))
     sub1=input("enetr your first subject : ")
     sub2=input("enetr your second subject : ")
     sub3=input("enetr your third subject : ")
     date=int(input("enter your birth date: "))
     month=input("enter your birth month like oct,jun: ")
     year=int(input("enter your yaer of birth: "))
     date_of_birth=(date,month,year)
     subjects=[sub1,sub2,sub3]
     skills1=input("skill one python programing for example: ")
     skills2=input("skill 2")
     skills3=input("skill 3")
     skills={skills1,skills2,skills3}
     return name,age

details=student_details()



def student_list():
    student_list={details,course}
    print(student_list)


course=input("enter your course: ")

student_list()



#2

def total_marks():
     python=59
     mathematics=67
     science=87
     total_marks=python+mathematics+science
     print(total_marks)
     return total_marks
sum=total_marks()

def average_marks():
     average_marks=sum/3
     print(average_marks)
     
