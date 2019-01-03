#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 8
import math
x=1
y=1
print("Please enter a non-empty sequence of positive integers, each one on a separate line. End your sequence by typing -1: "))
while(x!=-1 and x>0):
    x = int(input())
    if (x!=-1):
        y=y*x
mean = math.pow(y,(1/3))
print("The geometric mean is: "+ str(mean))
