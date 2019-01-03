#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 6
a = int(input("Enter a positive integer, a: "))
b = int(input("Enter a positive integer, b: "))
quotient = 0
remainder = a
x=a
y=b
while(x>y):
    x-=y
    quotient+=1
for i in range (1,quotient):
    remainder -=b 

print("The quotient of "+str(a)+" divided by "+str(b)+" is "+str(quotient)+" and the remainder is "+str(x))
