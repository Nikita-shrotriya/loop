num=int(input("enter the number"))
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(num,"is a prime number")
else:
    print(num,"is a not prime number")