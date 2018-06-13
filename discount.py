price=int(input(" enter the price of jeans:Rs."))
quantity=int(input(" enter the no. of jeans:"))
amount=price*quantity
if amount >2000:
    print("yaaa.... 20% discount is appicable!")            
    discount=amount*20/100
    amount=amount-discount
elif amount>1000:  
      print("ohh... 10% discount is applicable!")
      discount=amount*10/100
      amount=amount-discount
else:
    print("thank's for shopping.!")          
print("your total amount is: Rs.",amount)             
