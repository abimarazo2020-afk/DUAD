'''#EJERCICIO#1
Create two functions that print two different things, and have the first one call the second one.'''

def function_one():
    print('This is my function one')


def function_two():
    print('this fucntion is calling my first function')
    function_one()

function_two()

# R/
# this fucntion is calling my first function
# This is my function one





'''EJERCICIO#2
Experiment with the concept of scope:
Try accessing a variable defined inside a function from outside.
Try accessing a global variable from within a function and changing its value.
'''

variable_two = 95


def function_three():
    global variable_two
    variable_two = 100
    variable_one = 55
    print(variable_one)
    print(variable_two)
    

function_three()
print(variable_two) # aqui el resultado es 95 porque solo se cambia dentro de la funcion

#print(variable_one)  # "variable_one" is not defined







'''EJERICICIO#3
Create a function that returns the sum of all the numbers in a list.

The function will take one parameter (the list) and return a number (the sum of all its elements).

[4, 6, 2, 29] → 41'''


def function_four(list_one):
    counter = 0
    for number in list_one:
        counter += number

    return counter

print(function_four([1, 2, 3, 4, 5]))






'''EJERICICIO#4
Create a function that reverses a string and returns it.

We already did this with iterables.

“Hello world” → “odnum aloH”
'''

def reverse_function(second_variable = 'Abigail'):
    reverse_string = ''
    for caracter in range(len(second_variable)-1, -1, -1):
        reverse_string += second_variable[caracter] #el elemento del indice caracter

    return reverse_string

result = reverse_function()
print(result)






'''EJERICICIO#5
Create a function that prints the number of uppercase letters and the number of 
lowercase letters in a string.'''


def uppercase_and_lowercase_function(my_string = 'El Barcelona Gano'):
    upper = 0
    lower = 0


    for caracter in my_string:
        if caracter.isupper():
            upper += 1

        elif caracter.islower():
            lower += 1

    return upper, lower



print(uppercase_and_lowercase_function())

   

'''EJERCICIO#6
Create a function that accepts a string of words separated by hyphens and returns the same string, 
but sorted alphabetically.
It needs to be converted to a list, sorted, and then converted back to a string.

“python-variable-function-computer-monitor” → “computer-function-monitor-python-variable”'''


def strings_with_words_function(big_string):



     list_three = big_string.split('-')
     list_three.sort()
     return '-'.join(list_three) #join convierte a string again

result =  strings_with_words_function('Mouse-computer-art-pencil')
print(result)

    

'''EJERCICIO#7
Create a function that accepts a list of numbers and returns a list of the prime numbers in that list.

[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Research the mathematical logic for determining if a number is prime and translate it into code. 
Don't look for the code itself; that won't help.

Tip 2: This involves several steps (iterating through the list, checking if each number is prime, and adding it to another list). 
Therefore, it's best to add another function to check if the number is prime or not.
'''


def is_prime(n):
    if n <= 1:
        return False #quita los negativos y menores que 1
        

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True



def prime_numbers_function(list_numbers = [1, 2, 3, 4, 5, 11, 12, 13]):
    primes = []
    for number in list_numbers:
        if is_prime(number):
            primes.append(number)

    return primes


