product_price = float(input("Enter the product price: "))
discount = 0
total_price = 0
print()

if(product_price < 100):
    discount = product_price * 0.02
    total_price = product_price - discount
    print (f"the price of your product with the 2% discount is {total_price}")
elif(product_price >= 100):
    discount = product_price * 0.1
    total_price = product_price - discount
    print (f"the price of your product with the 10% discount is {total_price}")