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



'''EJERCICIO#2
Create a program that checks if all elements in a list are positive
Restrictions:
Do not use functions like all()'''


list_two = [1, -3, -15, 56, 8, 9]
positive_elements = []

for elem in list_two:
    if elem > 0:
        positive_elements.append(elem)

    else:
        break

if len(positive_elements) == len(list_two):
    print(True)
    print('All the number are positive')
else:
    print(False)
    print("Not all the number are positive")





'''EJERCICIO#3
Write a program that displays the smallest value in a list without using `min()`. 
Use a variable to compare one value to another.'''


list_three = [56, 6, 84, 8, 2, 1]
min_value = 56

for value in list_three:
    if value < min_value:
        min_value = value

print(f'"The lowest value is {min_value}"')




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





'''EJERCICIO#5
Create a program that asks the user to enter 5 words. 
Then display a new list with only those words that have more than 4 letters.'''

words_counter = 1
list_five = []
new_list_five = []

while words_counter <= 5:
    words = str(input(f'Enter your word {words_counter}:'))
    list_five.append(words)
    words_counter += 1


for word in list_five:
    if len(word) > 4:
        new_list_five.append(word)

print(new_list_five)
















