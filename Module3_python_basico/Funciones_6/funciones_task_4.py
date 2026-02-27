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
