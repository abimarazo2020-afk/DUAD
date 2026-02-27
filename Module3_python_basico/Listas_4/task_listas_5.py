
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