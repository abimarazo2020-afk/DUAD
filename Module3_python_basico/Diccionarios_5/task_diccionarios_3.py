'''EJERCICIO#3
Create a program that uses a list to remove keys from a dictionary.
'''

list_three = ['key_1', 'key_2', 'key_3']

dictionary = {}

#llenar el diccionario
for key in list_three:
    dictionary[key] = None

#Elimina del dicionario
for key in list_three:
    dictionary.pop(key, None)

print(dictionary)
