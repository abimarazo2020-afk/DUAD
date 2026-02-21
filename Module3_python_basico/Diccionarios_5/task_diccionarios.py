'''EJERCICIO#1:
Create a dictionary that stores the following information about a hotel:
name
number_of_stars
rooms
The value of the rooms key should be a list, and each room should have the following information:
number
floor
price_per_night'''



hotel_information = {
    'name': 'The Nexus Hotel',
    'number_of_stars': 5,
    'rooms': [
        
        {
            'number': 1,
            'floor': 1,
            'price_per_night': 30
        },

        {
            'number': 2,
            'floor': 1,
            'price_per_night': 30
        },

        {
            'number': 3,
            'floor': 1,
            'price_per_night': 30
        }
    ]
}








'''EJERCICICIO#2
Create a program that creates a dictionary using two lists of the same size, 
using one for its keys, and the other for its values.
Examples:
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
→ {'first_name': 'Alek', 'last_name': 'Castillo', 'role': 'Software Engineer'}
'''


list_one = ['ID', 'ROLE', 'LOCATION']
list_two = ['Aab', 'IT', 'Heredia']

diccionario = {}

#llena el dicionario 
for i in range(len(list_one)):
    diccionario[list_one[i]] = list_two[i]

print(diccionario)






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
