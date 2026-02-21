'''EJERCICIO#1
Create a program that:
Asks the user for their name
If the name is numeric (isdigit()), raises ValueError("The name cannot be a number")
Then ask for their age.
If it's not a valid number, capture the ValueError and display a message.
If everything goes well, print a message: "Hello <name>, your age is <age>"
'''

print('Hello this is the program')

try:
    name = input(f'Ingrese su nombre:')
    if name.isdigit():
        raise ValueError('The name cannon be a number')
    
    age = int(input('ingrese su edad:'))
    print(f'Hello {name}, your age is {age}')

except ValueError as error:
    print(f'This is not a valid number, {error}')



'''EJERCICIO#2
Create a function `convert_to_integer(list)` that:
Receives a list of strings
Attempts to convert each element to an integer using `int()`
Uses `try-except` to catch errors (`ValueError`)
If any element cannot be converted, displays "Could not convert element: <value>" and continues with the others'''


def convert_to_integer(string_list):
    converted = []
    
    for string in string_list:
        try:
            converted.append(int(string))
        
        except ValueError as error:
            print(f'Couldnt convert string: {string}')
       
    return converted
 
result = convert_to_integer(['pencil', 'computer', 'cpu', 'door', 'kitchen'])
print(result)



'''Create a function `sum_values(list)` that:
Receives a list of elements (strings, integers, mixed floats)
Attempts to convert each element to type `float`
If successful, sums the value and displays: "<value> summed successfully"
If unsuccessful, displays: "Invalid element: <value>"
Finally, prints the total sum'''

def sum_values(list_sum):

    total_floats = 0
    for value in list_sum:

        try:
            total_floats += float(value)
            print(f'{value} summed successfully')

        except ValueError as error:
            print(f'Invalid element: {value}, {error}')

    
    return total_floats

result = sum_values(['5', 'hello', 9, 'here', 8, 8.2])
print(result)

