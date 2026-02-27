'''EJERCICIO#1
Create a program that counts how many times a specific number appears in a list.
 Ask the user for a list of numbers and another number to search for.
'''
counter = 1
list_one = []

while counter <= 10:
    number = int(input(f'Enter the number: {counter}:'))
    list_one.append(number)
    counter += 1

print(f'Your list of number are: {list_one}')
number_to_search = int(input('Enter the number to look for:'))


counter_two = 0

for num in list_one:
    if number_to_search == num:
        counter_two += 1

print(f'the number {number_to_search} was on repeat: {counter_two} times')



















