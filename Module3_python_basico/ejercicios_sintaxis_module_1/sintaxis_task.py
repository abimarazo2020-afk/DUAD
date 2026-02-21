#Ejericios de Sintaxis:

""" #EJERCICIO#1

Experiment by adding different types of data and write down the results.

"""

print('abigail' + 15) #error no se puede sumar un str y un int
print('abigail' + ' ' , 'azofeifa')
print([1,5,7] + 15) #error no se puede sumar una lista con un int, deberia de ser list tambien
print([8,5,7] + [15])
print(2.5 + 2)
print(True + True)
print(True + False)
print(False + False)


""" EJERCICIO#2
Create a program that asks the user for their first name, last name, and age.
Display whether they are a baby, child, preteen, teenager, young adult, adult, or senior citizen.
"""

name = input('Enter your name:')
last_name = input('Enter your last name:')
age = int(input('Enter your age:'))

if(age <= 6):
    print('You are a baby')

elif(age <= 12):
    print('You are a child')

elif(age <= 18):
    print('You are a teenager')

elif(age <= 35):
    print('you are a young adult')

elif(age < 65):
    print('you are an adult')

else:
    print('you are an older adult')

print(f'Your name is {name} {last_name} and your age is: {age}')


"""EJERCICIO#3
Create a program with a secret number from 1 to 10. The program should not close until the user guesses the number.
You must research how to generate a different random number each time the program runs.
"""

import random


secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input('guess the secret number (1 al 10):'))
    if guess != secret_number:
     print('Incorrect, keep trying.')

print(f'correct, the secret number is {secret_number}')


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


"""EJERICIO#5
Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.
"""

total_notes = int(input('Ingrese su cantidad de notas:'))
note_counter = 1
disapproved_quantity = 0
approved_quantity = 0
approved_average = 0
disapproved_average = 0
total_average = 0
total_sum = 0
approved_sum = 0
disapproved_sum = 0
#si solo ponemos una suma esta mal porque no cuenta los valores de las notas si no la cantidad de notas


while note_counter <= total_notes:
    current_note = int(input(f'Enter your note #{note_counter}:'))
    note_counter = note_counter+1
    total_sum = total_sum + current_note

    if(current_note >= 70):
        approved_quantity = approved_quantity + 1
        approved_sum = approved_sum + current_note

    else:
        disapproved_quantity = disapproved_quantity + 1
        disapproved_sum = disapproved_sum + current_note


total_average = total_sum / total_notes
print(total_average)

if approved_quantity > 0:
    approved_average = approved_sum / approved_quantity

if disapproved_quantity < 0:
    disapproved_average = disapproved_sum / disapproved_quantity


print(f'The student has this number of passing grades. {approved_quantity}')
print(f'The student has this number of failing grades {disapproved_quantity}')
print(f'The average passing grade is:: {approved_average}')
print(f'The average number of failing grades is: {disapproved_average}')
print(f'This is the overall average {total_average}')



