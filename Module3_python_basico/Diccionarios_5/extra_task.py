'''#EJERCICIO#1
Given a sales list with the following information:
date
customer email
items
And each item having the following information:
name
UPC
unit_price
Create a dictionary that stores the total sales for each UPC.'''

sales = [
    {
        'date': '12/05/2025',
        'customer_email': 'adriana@gmail.com',
        'items': [
            {
            'name': 'milk',
            'upc': 'UPC-2211',
            'unit_price': 10.2


            },

            {
            'name': 'coffe',
            'upc': 'UPC-0013',
            'unit_price': 3.5
            },

            {
            'name': 'sugar',
            'upc': 'UPC-0015',
            'unit_price': 5
            }

        ]
    },
    
    {
        'date': '12/18/2025',
        'customer_email': 'maria@gmail.com',
        'items': [
            {
            'name': 'onions',
            'upc': 'UPC-2200',
            'unit_price': 3.0
            },

            {
            'name': 'coffe',
            'upc': 'UPC-0013',
            'unit_price': 3.5
            },

            {
            'name': 'salt',
            'upc': 'UPC-0009',
            'unit_price': 2
            }
        ]
    },

    {
        'date': '12/30/2025',
        'customer_email': 'oscar@gmail.com',
        'items': [
            {
            'name': 'coffe',
            'upc': 'UPC-0013',
            'unit_price': 3.5
            },

            {
            'name': 'salt',
            'upc': 'UPC-0009',
            'unit_price': 2
            },

            {
            'name': 'watermelon',
            'upc': 'UPC-0005',
            'unit_price': 4
            }
        ]
    }
]


totales_upc = {}

for sale in sales:
    for product in sale['items']:
        upc = product['upc']
        price = product['unit_price']
        
        totales_upc[upc] = totales_upc.get(upc, 0) + price # totales_upc[upc] hace que upc sean las keys del dict
        #parte derecha: Dame el valor de este upc” , Si no existe, devuelve 0
        # price suma el precio actual
        #totales_upc[upc] =  Guarda el nuevo total para ese UPC. upc seria las keys.

print(totales_upc)


'''upc va a agarrar el valor de la key y price va a agarrar el valor del value'''




'''EJERCICIO#2
Group employees by department
Given a list of employees where each has a name, email, and department, create a dictionary that groups the employees by their department:
'''


employes = [
    {
        'name': 'Myron',
        'email': 'myron@cisco.com',
        'department': 'Managment'
    },

    {
        'name': 'Diego',
        'email': 'diego@cisco.com',
        'department': 'SME'
    },


    {
        'name': 'jeremy',
        'email': 'Jeremy@cisco.com',
        'department': 'SME'
    },

    {
        'name': 'Liseth',
        'email': 'liseth@cisco.com',
        'department': 'managment'
    },


    {
         'name': 'Andres',
        'email': 'Andres@cisco.com',
        'department': 'TSE'

    }


]


new_dictionary = {}


for employee in employes:
    department = employee['department']

    if department not in new_dictionary:
       new_dictionary[department] = []

    new_dictionary[department].append(employee)

print(new_dictionary)







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


