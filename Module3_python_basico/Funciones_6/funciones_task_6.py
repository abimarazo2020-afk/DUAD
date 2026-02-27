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