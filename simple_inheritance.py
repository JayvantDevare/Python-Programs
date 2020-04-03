#Inheritance program in Python
#Inheritance enable us to define a class that takes
#all the functionality from parent class and allows us to add more.
#In this program, you will learn how to use inheritance in Python.

print("Inheritance program in Python")

#Base Class - College

class College:
    def __init__(self):
        self.collegename="MITAOE"
        self.address="Alandi"

    def printData(self):
        print("College Information")
        print("College Name : ",self.collegename)
        print("College Address :",self.address)

#Derived Class Student -  which inherit Base class College
#All members of base call get automatically inherited in derived class
        
class Student(College):
    def __init__(self):
        self.sname="Akon"
        self.rno=101
        College.__init__(self)   #inherting constructor of Base class

    def printStudentData(self):
        #self.printdData()  here also you can access members of base class
        print("Student Name",self.sname)
        print("Student Roll Number",self.rno)
    
        
s1=Student()  #create object of derived class

#calling function of Base class using derived class object
s1.printData() #using derived class object we can access function of both derived as well as base class

#calling function of derived class using object of derived class
s1.printStudentData()
        
