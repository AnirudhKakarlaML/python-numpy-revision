''''class BankAccount:
    def __init__(self , balance):
        self.__balance = balance
    def deposit(self , amount):
        self.__balance+=amount
    def withdraw(self , amount):
        if(self.__balance>amount):
            self.__balance = self.__balance  - amount
        else:
            return f"Insufficient balance"
    def show_balance(self):
        print(self.__balance)
b1 = BankAccount(50000)
b1.deposit(2000)
b1.withdraw(2000)
b1.show_balance()
'''

'''class Student:
    def __init__(self):
        pass
        
    def set_marks(self , marks):
        self.__marks = marks
    def get_marks(self):
        print(f"The Marks are {self.__marks}")
s1 = Student()
s1.set_marks(92)
s1.get_marks()
'''

'''class Animal:
    def eat(self):
        print("Animal Is Eating")
class Dog(Animal):
    def bark(self):
        print("Dog Is BArking")
d1 = Dog()
d1.eat()
d1.bark()'''

'''class Person:
    def __init__(self , name):
        self.name = name
class Student(Person):
    def __init__(self ,name , roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print(f"The Name Of Student is {self.name} and roll_no is {self.roll_no}")
p1 = Person("Anirudh")
s1 = Student("Anirudh",793)
s1.display()

'''

'''class vehicle:
    def start(self):
        print("vehicle Started")
class car(vehicle):
    pass

v1 = vehicle()
c1 = car()
c1.start()'''

'''class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name , salary , department):
        self.department = department
        super().__init__(name , salary)
    def display(self):
        print(f"{self.name} , {self.salary} , {self.department}")
m1 = Manager("Anirudh" , 210000 , "Automation In Ai")
m1.display()

 '''

'''class Vehicle:
    def move(self):
        print("vehicle is moving")
class Car(Vehicle):
    def move(self):
        super().move()
        print("Car Is Started")
c1 = Car()
c1.move()'''

#ML Style Class
''''class LinearModel:
    def __init__(self , model_name):
        self.model_name = model_name
    def fit(self):
        print(f"Training {self.model_name} Model")
    def predict(self):
        print("Predicting...............")
    def score(self):
        print("Evaluating Model")
L1 = LinearModel("Logistic Regression")
L1.fit()
L1.predict()
L1.score()'''

'''class Battery:
    def charge(self):
        print("Battery Is Charging")
class Device:
    def __init__(self , brand):
        self.brand = brand
class Laptop(Device):
    def __init__(self , brand):
        self.battery = Battery()
        super().__init__(brand)
    def display(self):
        print(f" Brand : {self.brand}")
l1 = Laptop("Asus")
l1.display()
l1.battery.charge()'''

'''from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def start(ABC):
        pass
class Car:
    def start(self):
        print("Car Started")
class Bike:
    def start(self):
        print("Bike Started")
c1 = Car()
b1 = Bike()
c1.start()
b1.start()
        
        '''

'''from abc import ABC , abstractmethod
class Employee(ABC):
    @abstractmethod
    def caluculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self , name , monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
    def caluculate_salary(self):
        return self.monthly_salary*12
class PartTimeEmployee(Employee):
    def __init__(self , name ,hours_worked, hourly_rate):
        self.name = name
        self.hours_worked=hours_worked
        self.hourly_rate = hourly_rate
    def caluculate_salary(self):
        return self.hours_worked * self.hourly_rate
f1 = FullTimeEmployee("Anirudh", 50000)

p1 = PartTimeEmployee("Rahul", 80, 500)

print(f1.caluculate_salary())
print(p1.caluculate_salary())'''



        
    