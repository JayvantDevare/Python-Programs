# concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name
#Polymorphism -Method Overriding program in Python
#Method Overriding allows you to write same function/method definition in base class as well as in derived class.
#in this example we are overriding printData() method

print("\nMethod Overriding program in Python")

#Base Class - University

class University:
    def __init__(self):
        self.uninversityename="SPPU"
        self.address="Pune"

    def printData(self):
        print("\n****University Information****\n")
        print("University Name : ",self.uninversityename)
        print("University Address :",self.address)
        
#derived Class  College - which inherit Base class  University
 
class College(University):  #deriving base class University
    def __init__(self):
        self.collegename="MITAOE"
        self.address="Alandi"
        University.__init__(self) #inherting constructor of University Base class

    def printData(self):
        super().printData()   #call base class printData() of University class
        print("\n****College Information****\n")
        print("College Name : ",self.collegename)
        print("College Address :",self.address)

#Derived Class Student -  which inherit Base class College
#All members of base call get automatically inherited in derived class
        
class Student(College):  #deriving base class College as well as University
    def __init__(self):
        self.sname="Akon"
        self.rno=101
        College.__init__(self)   #inherting constructor of College Base class
       

    def printData(self):
        super().printData() #call base class printData() of College class
        print("\n****Student Information****\n")
        print("Student Name",self.sname)
        print("Student Roll Number",self.rno)
    
        
s1=Student()  #create object of derived class

#it will call all class method which is overriden
s1.printData()
        
