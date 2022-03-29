num=int(input("enter the number"))
i=0
r=0
while num>0:
    i=num%10
    r=r*10+i
    num=num//10
print(r)