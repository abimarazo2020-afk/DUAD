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







