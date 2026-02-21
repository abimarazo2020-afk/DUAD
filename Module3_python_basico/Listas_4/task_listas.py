''''EJERICIO#1
Create a program that iterates through 
and prints the values ​​of two lists of the same size at the same time.'''

first_list = ['today', '26', 'the day is']
second_list = ['is', 'of december', 'cloudy']

if len(first_list) == len(second_list):
    for i in range(len(first_list)):
        print(f'the element of the list 1: {first_list[i]}, element of the 2 list: {second_list[i]}') #poner el indice dentro de la variable hace  que imprima el elemento no el indice

else: 
    print("the lists doesn't match the lenght") 



'''EJERCICIO#2
Create a program that iterates through and prints a string letter by letter from right to left.
Hint: Research other ways to use the range function.
'''

my_string = 'Good afternoon friends'
print(len(my_string)) 

for character in range(len(my_string) - 1, -1, -1): #el primer -1 es porque en los strings el ultimo cracter es el -1
    print(my_string[character])





'''EJERCICIO#3
Create a program that swaps the first and last elements of a list.
 It should work with lists of any size.
 Ejemplos:
my_list = [4, 3, 6, 1, 7] → [7, 3, 6, 1, 4]
'''

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # R/ 5 -1

my_list[0], my_list[-1] = my_list[-1], my_list[0]





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





'''EJERCICIO#5
Create a program that asks the user for 10 numbers, and at the end displays all the numbers entered,
 followed by the highest number entered.
Examples:
86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. The highest was 86.
# '''

counter_number = 1
number = 0
list_one = []

while counter_number <= 10:
    number = int(input(f'Enter your number {counter_number}:') )
    list_one.append(number)
    counter_number += 1

print(list_one)
print(f'the highest was {max(list_one)}')

