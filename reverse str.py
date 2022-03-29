str=(input("enter"))
rev=""
count=len(str)
while count>0:
    rev=rev+str[count-1]
    count=count-1
print(rev)