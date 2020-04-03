#Program to create class and data members and member functions

print("Program to create class and data members and member functions in python")
class Student:     #class Student
    sname="Akon"    #data members of class student
    rno=101
    
#function to print values of data members
    def printData(self): 
        print("Student name: ",self.sname)  
        print("Student Roll Number: ",self.rno)

#function to accept/assign values of data members from user
    def inputData(self,sname,rno):  
        self.sname=sname
        self.rno=rno
 
#creating object 
s1=Student()   

#printing student information using printData() 
print("Student details")
s1.printData()

#accepting values from user
sname=input("Enter student name")
rno=int(input("Enter Roll Number"))

#calling function inputData() by passing values
#which will assign user values to data members
s1.inputData(sname,rno)

#printing student information using printData() after assigning values by inputdata()

s1.printData()



