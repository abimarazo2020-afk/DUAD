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