
#**************************************Methord overriding*************************************

class Animal:
    def move(self):
        print("Animal walks")
class Frog(Animal):                           
    def move(self):                             #same methord but different implimentation called methord overriding
        print("Frog jumps")
# frog=Frog()
# frog.move()      

        #output
        # Frog jumps

#******************************************************
class Animal:
    def sound(self):
        print("Animal making sound")
class Cat(Animal):
    def sound(self):
        print("Meow")
class Dog(Animal):
    def sound(self):
        print("Woff")


# cat=Cat()
# cat.sound()
# dog=Dog()
# dog.sound()       
            
            #output
            # Meow
            # Woff


#**********************************************************************************

class Vehicle:
    def start(self):
        print("vehicle starting")
class Car(Vehicle):
    def start(self):
        print("car starts using keys")
class Electric_bike(Vehicle):
    def start(self):
        print("Bike starts by push button") 
# car=Car()
# car.start()
# electric_bike=Electric_bike()
# electric_bike.start()     

                #output
                # car starts using keys
                # Bike starts by push button/


