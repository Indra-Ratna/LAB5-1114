#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 4

terms = int(input("Enter a positive integer: "))
v1 = 1
v2 = 1
count = 0
while(count<terms):
    print(v1,end=" ")
    new = v1+v2
    v1=v2
    v2=new
    count+=1
