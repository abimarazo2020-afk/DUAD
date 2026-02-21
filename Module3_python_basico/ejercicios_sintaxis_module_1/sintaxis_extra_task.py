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
    




"""EJERCICIO#2
Create pseudocode that asks the user for a time in seconds and calculates whether it is less than or greater than 10 minutes.
If it is less, display how many seconds are needed to reach 10 minutes. If it is greater, display "Greater than".
If it is exactly equal, display "Equal".
"""

time_in_seconds = int(input('Enter your time in seconds:'))
missing_seconds = 0

if(time_in_seconds < 600):
    missing_seconds = (600 - time_in_seconds)
    print(f'The seconds that would be missing are{missing_seconds}')

elif(time_in_seconds > 600):
    print('Major')

else:
    print('Same')




"""Ejericicio#3
Create an algorithm that asks the user for a number, and then adds each number from 1 up to that number.
Then display the result of the sum.
"""

number = int(input('Enter the number:'))
counter = 1
addition = 0

while counter <= number:
    addition = addition + counter 
    counter = counter + 1 

print(f'the sum from 1 to {number} entered is: {addition}')





"""EJERCICIO#4
Create a flowchart that has a secret number from 1 to 10, and asks the user to guess that number. 
The algorithm should not end until the user guesses the number.
"""

secret_number = 8
number = 0

print('Enter your number:')

while(number != secret_number):
    print('Incorrect, keep guessing the secret number')

print(f'Correct, this is the secret number: {secret_number}')






"""EJERCICIO#5
Create a flowchart that asks the user for 3 numbers. 
If one of those numbers is 30, or if the sum of the 3 numbers is 30, display “Correct”. 
Otherwise, display “Incorrect”.
"""

number1 = int(input('Enter the number1:'))
number2 = int(input('Enter the number2:'))
number3 = int(input('Enter the number3:'))
addition = number1 + number2 + number3

if(number1 == 30):
    print('Correct')

elif(number2 == 30):
    print('Correct')

elif(number3 == 30):
    print('correct')

elif(addition == 30):
    print('correct')

else:
    print("incorrect")






"""EJERCICIO#6
Temperature unit converter
Ask the user to enter a temperature in Celsius. 
Convert it to Fahrenheit and Kelvin. Display all three values.
"""
Fahrenheit = 0
Kelvin = 0

celsius_temperature = float(input('Enter your temperature in celsius:'))
Fahrenheit = (celsius_temperature * 9/5) + 32
Kelvin = celsius_temperature + 273.15

print(f'The temperature in Celsius is: {celsius_temperature} , The temperature in Fahrenheit is {Fahrenheit} and the temperature in Kelvin is {Kelvin}')






"""EJERCICIO#7
Custom Multiplication Table
Ask the user for a number from 1 to 10
Display their multiplication table from 1 to 12
"""

print('Welcome to your custom multiplication table')

number = int(input("Enter your numbre from  1 to 10:"))
mutiplication_result = 0

for i in range(1, 13): # i hacer referencia a cada uno de los index y el rango para iterar del 1 al es ese del 1 al 13 
    mutiplication_result = number * i
    print(f'{number} x {i} = {mutiplication_result}')

print('Fin')
