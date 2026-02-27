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