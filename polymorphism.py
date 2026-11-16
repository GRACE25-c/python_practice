
#*********************Polymophism********************************

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self, name, age,emp_id,salary,joining_date):
        super().__init__(name, age)
        self.emp_id=emp_id
        self.salary=salary
        self.joining_date=joining_date
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("employee id: ",self.emp_id)
        print("salary : ",self.salary)
        print("joinnig date: ",self.joining_date)
class Father(Person):
    def __init__(self, name, age,no_of_children):
        super().__init__(name, age)
        self.no_of_children=no_of_children
    def display(self):
        print("no of children: ",self.no_of_children)
class Son(Person):
    def __init__(self, name, age,fathers_name):
        super().__init__(name, age)
        self.fathers_name=fathers_name
    def display(self):
        print("fathers name of children: ",self.fathers_name)
class Husband(Person):
    def __init__(self, name, age,wife_name,date_of_marrage):
        super().__init__(name, age)
        self.wife_name=wife_name
        self.date_of_marrage=date_of_marrage
    def display(self):
        print("wife name is : ",self.wife_name)
        print("date of marrage: ",self.date_of_marrage)



# emp = Employee("Jacob George",35,"DHP112",58000,"10/2/2005")
# emp.display()
# father=Father("George",78,2)
# father.display()
# son=Son("manual",13,"Jacob George")
# son.display()
# husband=Husband("Jacob George",35,"Mary","09/02/1996")
# husband.display()



                                                                    #output

                                                                    # Name:  Jacob George
                                                                    # Age:  35
                                                                    # employee id:  DHP112
                                                                    # salary :  58000
                                                                    # joinnig date:  10/2/2005
                                                                    # no of children:  2
                                                                    # fathers name of children:  Jacob George
                                                                    # wife name is :  Mary
                                                                    # date of marrage:  09/02/1996





#***************************************Task*************************************************

class Employee:
    def calculate_salary(self):
        print("Calculating employee salary")
class FullTimeEmployee(Employee):
    def calculate_salary(self):                         #methord overriding
        print("Full-time employee recivs a fixed monthly salary.")
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part-time employee salary is based on working hours.")
class Freelancer(Employee):
    def calculate_salary(self):
        print("Freelancer salary is based on completed projects.")

fulltimeemployee=FullTimeEmployee()
fulltimeemployee.calculate_salary()
parttimeemployee=PartTimeEmployee()
parttimeemployee.calculate_salary()
freelancer=Freelancer()
freelancer.calculate_salary()


                                        #output
                                        # Full-time employee recivs a fixed monthly salary.
                                        # Part-time employee salary is based on working hours.
                                        # Freelancer salary is based on completed projects.




                                        