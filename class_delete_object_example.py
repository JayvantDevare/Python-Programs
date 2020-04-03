#Program to delete object created in python 

print("Program to delete object created in python  ")
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

print("Deleting object in clearing the space allocated to object")

#Deleting object in clearing the space allocated to object

del s1           #it deletes object and clear the memory
s1.printData()


