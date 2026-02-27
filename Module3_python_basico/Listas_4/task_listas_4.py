
'''EJERICICIO#4
Create a program that removes all odd/impares numbers from a list.
Ejemplos:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]
'''

all_numbers = [1, 3, 5, 7, 2, 4, 6]
new_list = []

for number in all_numbers:
    if(number % 2 == 0):
        new_list.append(number)
       
print(new_list)


# para adivinar un impar hay que dividirlo entre 2, si retorna 0 es par y si retorna algo mas es impar
# Si el número es par → number % 2 da 0
# Si el número es impar → number % 2 da 1

