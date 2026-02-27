'''EJERCICIO#2
Create a program that iterates through and prints a string letter by letter from right to left.
Hint: Research other ways to use the range function.
'''

my_string = 'Good afternoon friends'
print(len(my_string)) 

for character in range(len(my_string) - 1, -1, -1): #el primer -1 es porque en los strings el ultimo cracter es el -1
    print(my_string[character])
