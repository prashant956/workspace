price=int(input("enter price:"))
quantity=int(input(" enter items:"))
amount=price*quantity
print("total amount.!",amount)
if amount>10000:
    print("yaa...10% discount is applicable")
    discount=amount*10/100
    print("total discount is",discount)
    amount=amount-discount

elif amount>5000:
        print("yaa..5% discount is applicabe")
        discount=amount*5/100
        print("total discount is",discount)
        amount=amount-discount

elif amount>2000:
            print("yaa...2% discount is applicable")
            discount=amount*2/100
            print("total discount is",discount)
            amount=amount-discount

elif amount>1000:
                print("yaa... 1% discount is applicable")
                discount=amount*1/100
                print("total discount is",discount)
                amount=amount-discount
else:
                    print(" thanks for shopping")
print("amount payable.!",amount)

