class BankAccount:
    def __init__(self,owner_name,bank_balance,account_type):
        self.owner_name=owner_name
        self.__bank_balance=bank_balance  #private
        self._account_type=account_type    #protected methord

    #to get the private attribute
    @property
    def bank_balance(self):         #chainging the methord privect as property
        return self.__bank_balance
    @property
    def account_type(self):            #methord name must be the wanted attribute name 
        return self._account_type


    #to update the value of privect attribute
    @bank_balance.setter
    def bank_balance(self,deposit_amt):
        self.deposit_amt=deposit_amt
        if deposit_amt<=0:                                                  #add the deposit into balance
            raise "Deposit amount cannot be zero or a negative value"
        self.__bank_balance=self.bank_balance+self.deposit_amt
    
    @account_type.setter
    def account_type(self,cheange_account):
        if cheange_account=="":
           raise ValueError("this account is already current account")       #cheanging the current account
        print(cheange_account)
        self._account_type = cheange_account


bankaccount=BankAccount("Grace Jacob",350000,"savings")

# print(bankaccount._account_type)            # savings   #jest passing the function not calling 
# print(bankaccount.__bank_balance)  #will get error
# print(bankaccount.bank_balance)   #350000   #privect attribute return that print like this 
# print(bankaccount.account_type)    #savings   #privect attribute return that print like this

        
        #Syntax: class.secter function = new value

# bankaccount.bank_balance=50000    #400000
# print(bankaccount.bank_balance)
# bankaccount.account_type="current"    #current
# print(bankaccount.account_type)

                        #output
                        # savings



#******************************************************Task******************************************************
class Employee:
    def __init__(self,employee_name,_department,__salary):
        self.employee_name=employee_name
        self._department=_department
        self.__salary=__salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self,up_salary):
        self.up_salary=up_salary
        if up_salary<=-1:
            raise "salary cannot be negative"
        self.__salary=self.up_salary
        
class Manager(Employee):
    def display_details(self):
        print(self.employee_name,"\n", self._department)
    @property
    def department(self):
        return self._department

# manager=Manager("Grace","Web development",50000)
# manager.display_details()

# print("Salary:", manager.salary)

# manager.salary = 600000
# print("Updated Salary:", manager.salary)


#*********************************************************************************************************************
class Vehicle:
    def __init__(self,vehicle_name,_rental_type,__rental_price):
        self.vehicle_name=vehicle_name
        self._rental_type=_rental_type
        self.__rental_price=__rental_price
    @property
    def rental_price(self):
        return self.__rental_price
    @rental_price.setter
    def rental_price(self,up_rental_price):
        self.up_rental_price=self.rental_price
        if up_rental_price<=0:
            raise "the updated rental price cannot be zero"
        self.__rental_price=up_rental_price
        print("updated rental price",self.__rental_price)
    def display_details(self):
        print(self.vehicle_name)
        print(self._rental_type)
        print(self.__rental_price)
        print(self.rental_price)
       

class Car(Vehicle):
    def calculate_rent(self,days):
        self.days=days
        print("total amont",self.rental_price*self.days)

    def display_details(self):
        print(self.rental_price)
        print(self.vehicle_name)
        print(self._rental_type)

class Bike(Vehicle):
    def calculate_rent(self,days):
        self.days=days
        print("total amont",self.rental_price*self.days)
        
    def display_details(self):
        print(self.vehicle_name)
        print(self._rental_type)
        print(self.__rental_price)


car=Car("Maruthi","4 weeler",2000)
bike=Bike("Activa","2 weeler",800)

car.display_details()
print(car.rental_price)

car.rental_price = 3000
print(car.rental_price)
# car.days=3
# bike.days=3
# car.calculate_rent()
# bike.calculate_rent()
car.calculate_rent(3)
bike.calculate_rent(3)


                            #output
                            # 2000
                            # Maruthi
                            # 4 weeler
                            # 2000
                            # updated rental price 3000
                            # 3000
                            # total amont 9000
                            # total amont 2400