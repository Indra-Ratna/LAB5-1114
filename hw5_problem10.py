#Indra Ratna
#CS-UY 1114
#05 Oct 2018
#Lab 5
#Problem 10

i=0
v=0
x=0
l=0
c=0
d=0
m=0

x = int(input("Enter decimal number: "))
val = x
val2 = x
while(val>1000):
    m=val//1000
    val = val%1000
while(val>500):
    d=val//500
    val = val%500
while(val>100):
    c=val//100
    val = val%100
while(val>50):
    l=val//50
    val = val%50
while(val>10):
    x=val//10
    val = val%10
while(val>5):
    v=val//5
    val = val%5
roman = (m*"M")+(d*"D")+(c*"C")+(l*"L")+(x*"X")+(v*"V")+(val*"I")
print(roman)
roman2=""
while(val2>1000):
    val2-=1000
    roman2+="M"
while(val2>500):
    val2-=500
    roman2+="D"
while(val2>100):
    val2-=100
    roman2+="C"
while(val2>50):
    val2-=50
    roman2+="L"
while(val2>10):
    val2-=10
    roman2+="X"
while(val2>5):
    val2-=5
    roman2+="V"
while(val2>0):
    val2-=1
    roman2+="I"
print(roman)


