n=int(input("enter"))
i=2
sum=1
while i<=n//2:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print(n,"is a perfact num")
else:
    print(n,"is not a perfact num")