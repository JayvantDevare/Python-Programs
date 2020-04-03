#Multiple Inheritance program in Python
#Inheritance enable us to define a class that takes
#all the functionality from parent class and allows us to add more.
#In this program, you will learn how to use Multilevel inheritance in Python.
#Multiple Inheritance - More than one base class and one derived class

print("\nMultiple Inheritance program in Python")

#Base Class - University

class University:
    def __init__(self):
        self.uninversityename="SPPU"
        self.address="Pune"

    def printUnivData(self):
        print("\n****University Information****\n")
        print("University Name : ",self.uninversityename)
        print("University Address :",self.address)
        
#Base Class - College

class College:
    def __init__(self):
        self.collegename="MITAOE"
        self.address="Alandi"

    def printClgData(self):
        print("\n****College Information****\n")
        print("College Name : ",self.collegename)
        print("College Address :",self.address)

#Derived Class Student -  which inherit Base class College and University
#All members of base call get automatically inherited in derived class
        
class Student(University,College):  #deriving base classes here University and College
    def __init__(self):
        self.sname="Akon"
        self.rno=101
        College.__init__(self)   #inherting constructor of College Base class
        University.__init__(self) #inherting constructor of University Base class

    def printStudentData(self):
        #self.printClgdData()  here also you can access members of base class
        print("\n****Student Information****\n")
        print("Student Name",self.sname)
        print("Student Roll Number",self.rno)
    
        
s1=Student()  #create object of derived class

#calling function of Base class using derived class object
s1.printUnivData()  #base class function

#calling function of Base class using derived class object
s1.printClgData() #using derived class object we can access function of both derived as well as base class

#calling function of derived class using object of derived class
s1.printStudentData()
        
