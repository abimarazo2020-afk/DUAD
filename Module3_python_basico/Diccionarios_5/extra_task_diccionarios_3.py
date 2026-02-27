'''EJERCICIO#3
Given a list of sold products, where each one has a category and price, create a dictionary 
that accumulates the total by category.
'''

second_dictionary = {}


products = [

    {'name': 'cpu', 'category':'Electronic', 'price': 300},
    {'name': 'mouse', 'category':'Electronic', 'price': 25},
    {'name': 'headset', 'category':'Electronic', 'price': 50},
    {'name': 'potatos', 'category':'food', 'price': 10},
    {'name': 'rice', 'category':'food', 'price': 7}
]



for product in products:
    category = product ['category']
    price = product ['price']

    if category not in second_dictionary:
        second_dictionary[category] = 0
        
    second_dictionary[category] += price

print(second_dictionary)


