'''EJERCICIO#2
Create a function `convert_to_integer(list)` that:
Receives a list of strings
Attempts to convert each element to an integer using `int()`
Uses `try-except` to catch errors (`ValueError`)
If any element cannot be converted, displays "Could not convert element: <value>" and continues with the others'''


def convert_to_integer(string_list):
    converted = []
    
    for string in string_list:
        try:
            converted.append(int(string))
        
        except ValueError as error:
            print(f'Couldnt convert string: {string}')
       
    return converted
 
result = convert_to_integer(['pencil', 'computer', 'cpu', 'door', 'kitchen'])
print(result)