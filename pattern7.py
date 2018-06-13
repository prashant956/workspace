n=int(input("enter a number:"))
k=n
for i in range(0,n):
    for j in range(0,k):
        print("*",end='')
    k=k-2
    print()
