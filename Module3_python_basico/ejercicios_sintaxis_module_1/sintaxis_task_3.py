"""EJERCICIO#3
Create a program with a secret number from 1 to 10. The program should not close until the user guesses the number.
You must research how to generate a different random number each time the program runs.
"""

import random


secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input('guess the secret number (1 al 10):'))
    if guess != secret_number:
     print('Incorrect, keep trying.')

print(f'correct, the secret number is {secret_number}')