
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
