a=input("enter the number")
i=0
s=" "
while i<len(a):
    if a[i]=="1":
        s=s+"one"
    if a[i]=="2":
        s=s+"two"
    if a[i]=="3":
        s=s+"three"
    if a[i]=="4":
        s=s+"four"
    if a[i]=="5":
        s=s+"five"
    i=i+1
print(s,end=" ")
