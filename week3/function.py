
def calculate_discount(price,discount_percent):
    
    if discount_percent>=20:
        final_price=price+(price*discount_percent)
        print(f"the total price is {final_price}") 
    
    else:
        print(f"the total price is {final_price}") 
    


calculate_discount(200,20)


def calculate_discount():
    
    price=float(input('enter the price of the item'))
    discount_percent=float(input('Enter the diacount of the item'))
    if discount_percent>=20:
        final_price=price+(price*discount_percent)
        print(f"the total price is {final_price}") 
    
    else:
        print(f"the total price is {final_price}") 
    
    
calculate_discount()    