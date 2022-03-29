n=int(input("enter"))
rev=0
x=n
while n>0:
    rev=rev*10+n%10

    n=n//10
if x==rev:
    print("palindrom")
else:
    print("not palindrom")