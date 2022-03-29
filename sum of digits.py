num=int(input("enter the number"))
i=0
sum=0
while num!=0:
    i=num%10
    sum=sum+i
    num=num//10
print(sum)