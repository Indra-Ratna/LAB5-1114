#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 9
dec = int(input("Enter decimal number: "))
remain = ""
x = dec
while(x>0):
    remain+=str(x%2)
    # remain = str(x%2) + remain
    x=x//2
remain=remain[::-1]
print("The binary representation of "+str(dec)+ " is "+remain)
