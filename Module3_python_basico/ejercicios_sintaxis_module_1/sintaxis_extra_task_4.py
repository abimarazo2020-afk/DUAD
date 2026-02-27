"""EJERCICIO#4
Create a flowchart that has a secret number from 1 to 10, and asks the user to guess that number. 
The algorithm should not end until the user guesses the number.
"""

secret_number = 8
number = 0

print('Enter your number:')

while(number != secret_number):
    print('Incorrect, keep guessing the secret number')

print(f'Correct, this is the secret number: {secret_number}')