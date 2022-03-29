n=int(input("enter"))
sum=0
num=n
while sum!=1 and sum!=4:
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**2
        n=n//10
    n=sum
if sum==1:
    print(n,"is a happy number")
else:
    print(n,"is not a happy number")