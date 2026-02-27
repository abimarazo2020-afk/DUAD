"""EJERCICIO#1
Create pseudocode that prompts the user for a product price, calculates the discount.
and displays the final price, taking into account the following:
If the price is less than 100, the discount is 2%.
If the price is greater than or equal to 100, the discount is 10%.
Examples:
120 → 108
40 → 39.2
"""

price = int(input(f'Enter the product price:'))
discount = 0
final_price = 0

if(price < 100):
    print('Your discount is 2%')
    discount = 0.02
    final_price = price - (price * 0.02)
    print(f'Its final price is {final_price}')
     
else:
    print('Your discount is 10%')
    discount = 0.10
    final_price = price - (price * 0.10)
    print(f'Its final price is {final_price}')
    

