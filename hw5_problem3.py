#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 3
x = int(input("Enter positive integer: "))
sum=0
for i in range (-11,x-1,3):
    print(str(i))
    sum+=i
print("The sum of the first "+str(x)+" terms of the sequence is "+str(sum))
