'''EJERCICIO#4
Create a program that receives a list of numbers and calculates the average of the values, 
then creates a new list with only the values ​​greater than the average.'''

#hay que hacer una suma de todos los valores y dividirlos entre la cantidad de valores

list_four = [50, 80, 40, 100, 20]
suma = 0
new_list_four = []

for element in list_four:
    suma += element

print(suma)
average = suma / len(list_four)

for element in list_four:
    if element > average:
        new_list_four.append(element)

print(new_list_four)
