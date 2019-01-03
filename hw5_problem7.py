#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 7

x = int(input("Enter a positive integer: "))
y=x
i=10
j = 1
sum1 = 0
val = 1
while(val>0):
    val = (y%i)//j
    j=i
    i*=10
    sum1+=val
print("The sum of the digits of "+str(x)+" is "+str(sum1))






while y>0:
    sum1 += y%10
    y //= 10

    
