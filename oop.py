'''class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name is {self.name} and age is {self.age}")
s1 = Student("Anirudh" , 21)
s1.display()'''

'''class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary*12
e1 = Employee("Anirudh" , 180000)
print(e1.annual_salary())'''

'''class Rectangle:
    def __init__(self , length , breadth ):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
r1 = Rectangle(1 , 2)
print(r1.perimeter())
print(r1.area())'''

'''
class Student:
    school = "XYZ"
    def __init__(self , name):
        self.name = name
s1 = Student("Anirudh")
s2 = Student("RAhul")
s3 = Student("YAsh")
print(s1.name , s1.school)
print(s2.name , s2.school)
print(s3.name , s3.school)
'''

'''class Employee:
    company = "google"
    @classmethod
    def change_company(cls , new_company):
        cls.company = new_company
e1 = Employee()
e1.change_company("Open AI")
print(e1.company)
'''

'''class Caluculator:
    @staticmethod
    def add(a , b):
        return a+b;
    @staticmethod
    def subtract(a , b):
        return a-b
    @staticmethod
    def multiply(a , b):
        return a*b
c1 = Caluculator()
print(c1.add(1 , 2) , c1.subtract(1 , 2) , c1.multiply(1 , 2))'''

