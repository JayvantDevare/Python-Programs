#Program to create class and objects
print("Program to create class and objects in python")
class Student:     #class Student
    sname="Akon"    #data members of class student
    rno=101

#creating object 
s1=Student()   
s2=Student()

print("Student details")

print("Student name: ",s1.sname)  #prinitng values of data members
print("Student Roll Number: ",s1.rno)

s2.sname="bkon"   #assigning values to the data members using object
s2.rno=102

print("Student details")

print("Student name: ",s2.sname)
print("Student Roll Number:",s2.rno)

''' output of current program
Program to create class and objects in python
Student details
Student name:  Akon
Student Roll Number:  101
Student details
Student name:  bkon
Student Roll Number: 102 '''
