
'''EJERCICIO#3
Write a program that displays the smallest value in a list without using `min()`. 
Use a variable to compare one value to another.'''


list_three = [56, 6, 84, 8, 2, 1]
min_value = 56

for value in list_three:
    if value < min_value:
        min_value = value

print(f'"The lowest value is {min_value}"')
