'''Create a function that takes a text string and a character, 
and returns how many times that character appears in the text.'''


def first_function():
    counter = 0
    word = input('Enter the word:')
    character = input('Enter the caracter you are looking for:')

    for i in word:
        if i == character:
            counter += 1

    print(f'The character was on repeat: {counter}')

first_function()













