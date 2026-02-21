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





''''EJERCICIO#2
Create a function that takes a list of words and a number n,
 and returns a new list with only the words that have more than n letters.
'''

def return_new_list_function(words_list, n):
    new_list = []
    for word in words_list:
        if len(word) >= n:
            new_list.append(word)

    return new_list

print(return_new_list_function(['Buenas', 'Tardes', 'Companeros'], 3))






'''EJERCICIO#3
Create a function that takes a string and returns how many vowels it contains.
'''

def vowels_function(My_string):
   vowels = 'aeiouAEIOU'
   contador = 0
   for letter in My_string:
       if letter in vowels:
           contador += 1

   return contador

print(vowels_function('Entendimiento'))
