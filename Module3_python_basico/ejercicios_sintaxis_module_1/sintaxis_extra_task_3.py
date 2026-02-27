"""Ejericicio#3
Create an algorithm that asks the user for a number, and then adds each number from 1 up to that number.
Then display the result of the sum.
"""

number = int(input('Enter the number:'))
counter = 1
addition = 0

while counter <= number:
    addition = addition + counter 
    counter = counter + 1 

print(f'the sum from 1 to {number} entered is: {addition}')
