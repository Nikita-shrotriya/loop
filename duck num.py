n=int(input("enter"))
i=0
while i<n:
    a=n%10
    n=n//10
    if a==0:
        i=i+1
if i>=1:
    print("duck number")
else:
    print("not duck number")