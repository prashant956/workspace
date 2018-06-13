year=int(input("enter a year:"))
n= int(input("enter a year:"))
for year in range(year,n):  
 if (year%4==0):
         print("%d is a leap year",year)
 elif (year%100==0):
         print("%d is a not a leap year",year)
 elif (year%400==0):
         print("%d is a leap year",year)
 else:
    print("%d is not a leap year",year)
