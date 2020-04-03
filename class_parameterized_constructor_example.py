#Program to create class and parameterized constructor in python 
#constructor are called as special fucntions
#special functions get automatically called when we create object of class
#constructors are used to initialize data members of class
#example     __init__(self):

print("Program to create class and parameterized constructor in python ")
class Student:
    def __init__(self,sname,rno):    #constructor with parameter
        self.sname=sname             #data members of class student initialized using constructor
        self.rno=rno    
        
#function to print values of data members
    def printData(self): 
        print("Student name: ",self.sname)  
        print("Student Roll Number: ",self.rno)

 
#creating object 
s1=Student("Dkon",202)    #calling of constructor automatically


#printing student information using printData() 
print("Student details")

s1.printData()





