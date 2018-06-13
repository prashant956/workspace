from math import sqrt
num=int(input("enter a no."))
sqr=int(sqrt(num)+1)
for var in range(2,sqr+1):
    if num%var==0:
        print("no is not prime")
        break
    elif var==sqr:
        print("no is prime")
