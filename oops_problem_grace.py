#OOP Project: Bank Account Management System
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,account_holder,_account_type,balance):
        self.account_holder=account_holder
        self._account_type=_account_type
        self.__balance=balance
    

    #getter
    @property
    def balance(self):
        return self.__balance
    #setter
    @balance.setter
    def balance(self,amount):
       
        if amount<0:
            raise "not allow negative balances "
        self.__balance=amount
    def  deposit(self,amount): 
        if amount<=0:
            print("Deposit amount must be positive")
            return
        self.balance=self.balance + amount
        print("Deposit successful:",amount)

    def withdraw(self,amount):
        if amount<=0:
            print("withdraw amount must be positive ")
            return
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Withdrawal successful:",amount)
        else:
            print("insufficient balance")
    
    def display_details(self):
        print(f"account holder: {self.account_holder}")
        print(f"account type: {self._account_type}") 
        print(f"Balance: {self.balance}")

    @abstractmethod
    def calculate_interest(self):
        pass  
class  SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance,"savings")       
        
    def calculate_interest(self):
       return self.balance*0.05
class CurrentAccount(BankAccount):    
    def __init__(self, account_holder,balance):
        super().__init__(account_holder,balance,"current")
        
    def calculate_interest(self):
        return self.balance*0.02


# Creating Accounts
grace=SavingsAccount("grace",10000)
rahul=CurrentAccount("rahul",20000)

#Banking Operations
grace.deposit(5000)
grace.withdraw(40000)

print()

rahul.deposit(40000)
rahul.withdraw(30000)

# Display Account Details
grace.display_details()
rahul.display_details()

print(f"grace's Annual Interest: Rs.{grace.calculate_interest()}")
print(f"Rahul's Annual Interest: Rs.{rahul.calculate_interest()}")
