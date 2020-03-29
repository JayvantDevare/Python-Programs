#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Program Arithmetic operations in Python
#
# Author:      jayvant devare
#
# Created:     29/03/2020
# Copyright:   (c) jayvant 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num1 = 10
num2 = 20

result = num1 + num2

print("Result is :",result)  #print

#print using .format() option
print ("Addition of  {0} + {1} is = {2}".format(num1,num2,result))

result = num1 - num2

print ("Substracation of  {0} - {1} is = {2}".format(num1,num2,result))

result = num1 * num2

print ("Multiplication of  {0} * {1} is = {2}".format(num1,num2,result))

result = num1 / num2

print ("Division of  {0} / {1} is = {2}".format(num1,num2,result))