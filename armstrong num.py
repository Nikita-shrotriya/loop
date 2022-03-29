num=int(input("enter"))
sum=0
arm=num
while num>0:
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if arm==sum:
    print("amstrong num")
else:
    print("not armstrong num")