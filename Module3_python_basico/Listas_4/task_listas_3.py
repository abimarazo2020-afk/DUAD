'''EJERCICIO#3
Create a program that swaps the first and last elements of a list.
 It should work with lists of any size.
 Ejemplos:
my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]
'''

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # R/ 5 -1

my_list[0], my_list[-1] = my_list[-1], my_list[0]
