from math import sqrt
start=int(input("enter starting point:"))
end=int(input("enter ending point:"))
count=0
for num in range(start,end+1):
    sqr=int(sqrt(num)+1)
    for var in range(2,sqr+1):
        if num%var==0:
            result=False
            break
        else:
            result=True
    if result:
        count+=1
        print(num,end=" ")
print()
print("total prime no are=%d"%count)
