#Program to create class and constructor in python 
#constructor are called as special fucntions
#special functions get automatically called when we create object of class
#constructors are used to initialize data members of class
#example     __init__(self):

print("Program to create class and default constructor in python ")
class Student:
   
    def __init__(self): #default constructor
        self.sname="Dummy"  #initializing data members using constructor
        self.rno=999
    
        
#function to print values of data members
    def printData(self): 
        print("Student name: ",self.sname)  
        print("Student Roll Number: ",self.rno)

 
#creating object 
s1=Student()     #calling of constructor automatically


#printing student information using printData() 
print("Student details")
s1.printData()





