student1="Grace"
student1_age=21
student2="Keerthi"
student2_age=22
student3="Krishnapriya"
student3_age=22
student4="Jayalakshmi"
student4_age=22
student5="Nice"
student5_age=21

# print("student 1",student1,"\nAge",student1_age)
# print("student 2",student2," \nAge",student2_age)
# print("student 3",student3,"\nAge",student3_age)
# print("student 4",student4,"\nAge",student4_age)
# print("student 5",student5,"\nAge",student5_age)

#********************how to define a class**************************************
class Student: #class student fist letter is always capital
    def __init__(self,name,age):
        self.name=name
        self.age=age
# stud1=Student("jhon",12)    #object created object is stud1
# print(stud1.name,"\n",stud1.age)  
# stud2=Student("grace",21)
# print(stud2.name,"\n",stud2.age)                         #defind caryagal aanu atribute  like name age
# stud3=Student("nice",21)
# print(stud3.name,"\n",stud3.age)
# stud4=Student("jacob",21)
# print(stud4.name,"\n",stud4.age)
# stud5=Student("george",21)
# print(stud5.name,"\n",stud5.age)


#********************************************************************************************
class Book:
    def __init__(self,name_of_book,author_name,year_of_release,no_of_pages):       #constrecter is a special type of function 
                                                                                    #that will be call when we try to innitialised (__init__)
        self.name_of_book=name_of_book
        self.author_name=author_name
        self.year_of_release=year_of_release           # atrbute are name_of_book,author_name,year_of_release,no_of_pages
        self.no_of_pages=no_of_pages
# book1=Book("entte katha","Madhavi kutti",2012,200)
# print(book1.name_of_book,"\n",book1.author_name,"\n",book1.year_of_release,"\n",book1.no_of_pages)
# book2=Book("entte jeevitham","Usha Prekash",2012,200)
# print(book2.name_of_book,"\n",book2.author_name,"\n",book2.year_of_release,"\n",book2.no_of_pages)
# book3=Book("sankalppam","john joseph",2012,200)
# print(book3.name_of_book,"\n",book3.author_name,"\n",book3.year_of_release,"\n",book3.no_of_pages)


#***************************************************************************************************
class Employee:
    age=10                    #defining class atributes (common data ) that dose not cheaing
    def __init__(self,name,salary,id_no,job_roll,joining_date):
        self.name=name
        self.salary=salary                                  #only perform calling the function 
        self.id_no=id_no                      #instence atriburtes
        self.job_roll=job_roll
        self.joining_date=joining_date

    def display_details(self):   #create a def in a class thats called methorde
            print("Name ",self.name,"\n","Salary",self.salary,"\n","id_no",self.id_no,"\n","job roll",self.job_roll,"\n","joinning date ",self.joining_date)
# emp1=Employee("Grace",400000,"210GHT","softwear developer","20/10/2026")
# emp1.display_details()
# # print("Name ",emp1.name,"\n","Salary",emp1.salary,"\n","id_no",emp1.id_no,"\n","job roll",emp1.job_roll,"\n","joinning date ",emp1.joining_date)
# emp2=Employee("Nice",500000,"2220GHT","HR","20/01/2024")
# emp2.display_details()
# # print("Name ",emp2.name,"\n","Salary",emp2.salary,"\n","id_no",emp2.id_no,"\n","job roll",emp2.job_roll,"\n","joinning date ",emp2.joining_date) 
# emp3=Employee("Jacob",100000,"110GHT","Web developer","02/10/2025")
# emp3.display_details()
# # print("Name ",emp3.name,"\n","Salary",emp3.salary,"\n","id_no",emp3.id_no,"\n","job roll",emp3.job_roll,"\n","joinning date ",emp3.joining_date) 
# emp4=Employee("Mary",200000,"130GHT","softwear developer","14/7/2024")
# emp4.display_details()
# # print("Name ",emp4.name,"\n","Salary",emp4.salary,"\n","id_no",emp4.id_no,"\n","job roll",emp4.job_roll,"\n","joinning date ",emp4.joining_date) 
# emp5=Employee("George",700000,"310GHT","softwear developer","20/10/2012")
# emp5.display_details()
# print(Employee.age)   #Accessing class atribute
# # print("Name ",emp5.name,"\n","Salary",emp5.salary,"\n","id_no",emp5.id_no,"\n","job roll",emp5.job_roll,"\n","joinning date ",emp5.joining_date)       

     

#*********************************PROBLEM BASED ON CLASS ATRIBUTE********************************************************************

class Student:
     count=0
     def __init__(self,name,age,height):
          self.name=name
          self.age=age               #constrecter
          self.height=height
          Student.count=Student.count+1   #incriment count by 1 when class has initialized
        
     def display_count(self):
        print(Student.count)

     def display_details(self):
        print("Name ",self.name,"\n","Age",self.age,"\n","Height",self.height)
        
# stu1=Student("Grace",21,5.05) 
# stu1.display_details()       
# stu2=Student("Nice",22,5.05) 
# stu2.display_details()       
# stu3=Student("Mary",21,5.05)   
# stu3.display_details()  
# stu3.display_count()      

    #uoutput will get like this 
    # Name  Grace 
    #  Age 21 
    #  Height 5.05
    # Name  Nice 
    #  Age 22 
    #  Height 5.05
    # Name  Mary 
    #  Age 21 
    #  Height 5.05
    # 3    
    
#***************************************inheritance*****************************************

# class Animals:
#     def __init__(self,has_leg):
#         self.has_leg=has_leg
# class Dog(Animals):   #here done a inheritance
#     pass
# dog= Dog(has_leg="yes")  
# print("the dog has 4 legs",dog.has_leg)  

#*************************************how to enterd new atributes******************************
class Animal:
    def __init__(self,sleep, eat):
        self.sleep=sleep
        self.eat=eat


class Dog(Animal):
    def __init__(self,sleep, eat, speek):
        super().__init__(sleep,eat)         #using this function we create a new atribute
        self.speek=speek


class Cat(Animal):
    def __init__(self,sleep,eat, speek):
        super().__init__(sleep,eat)
        self.speek=speek


# dog = Dog("yes", "yes", "Bow")
# cat=Cat("yes","yes","Meow")

# print(dog.sleep,dog.speek,dog.eat)
# print(cat.speek,cat.eat,cat.sleep)


# #***********************************task******************************************
# # #1
class Animal:
  #2
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print("the animal is eating")
       
        
class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")
        
        
class Cat(Animal):
    def meow(self):
        print("meow")


# dog = Dog("jack", 5)
# cat = Cat("kitty",2)
# print("name",dog.name,"\n","Age", dog.age)
# dog.bark()
# dog.eat()
# print("name",cat.name,"\n","Age",cat.age)
# cat.meow()
# cat.eat()

            #output

            # name jack 
            # Age 5
            # Woof! Woof!
            # the animal is eating
            # name kitty 
            # Age 2
            # meow
            # the animal is eating

# #*********************************************Task2***************************************************
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name,"\n","Age",self.age)
        
class Student(Person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course=course  
        

    def show_course(self):
        print(self.course)



# person=Person("Grace Jacob",21)
# Person.display(person)
# student=Student("Grace Jacob",21,"PGP DS & AI/ML")
# Student.show_course(student) 


            #output
            # Name Grace Jacob 
            # Age 21
            # PGP DS & AI/ML

# #****************************************Abstraction*********************************************
# #define a rool
from abc import ABC,abstractmethod
class Bank(ABC):     #abstract class ABC inherited

    @abstractmethod
    def deposite(self):
        pass                   # do not write any code inside the abstract class

    @abstractmethod
    def loan(self):
        pass

class SBI(Bank):

    def deposite(self):
        print("deposite is exicuted")     #abstract class mentioned all finction strictly present 
    def loan(self):
        print("loan is applied") 
    def profit(self):
        print("profit") 
# sbi=SBI()
# sbi.deposite()
# sbi.loan()  
# sbi.profit()

# #***************************************************TASK3**************************************************
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):     #created an abstraction methode 
        pass
class Rectangle(Shape):
        
    
    def __init__(self,length,width):
        
        self.length=length
        self.width=width
        print(length*width)
    def area(self):
        return self.length,self.width
            
               
        
class Circle(Shape):
    
    def __init__(self,radius):
        
        self.radius=radius
        print(3.14*radius*radius)                
    def area(self): 
        return self.radius          



rectangle=Rectangle(10,5)
circle=Circle(2.5)

#output
# 50
# 19.625