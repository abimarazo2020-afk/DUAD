"""EJERCICIO#4
Create a program that asks the user for three numbers and displays the largest one.
"""

number1 = int(input('Enter the number 1:'))
number2 = int(input('Enter the number 2:'))
number3 = int(input('Enter the number 3:'))

if(number1 > number2 and number1 > number3):
    print(f'the largest number is {number1}')

elif(number2 > number1 and number2 > number3):
    print(f'the largest number is {number2}')

else:
    print(f'the largest number is {number3}')