num=int(input("enter"))
sum=0
n=num
while n>0:
    i=1
    f=1
    r=n%10
    while i<=r:
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if sum==num:
    print("is a strong num")
else:
    print("is not a strong num")