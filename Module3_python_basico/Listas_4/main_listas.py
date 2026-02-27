'''Agregar datos'''
#Aqui utillizamos el metodo append para agregar

my_pets_list = [
	'dog',
	'cat',
]

my_pets_list.append('rabbit')
print(my_pets_list)


#R/

#[’dog’, ‘cat’, ‘rabbit’]

#codigo extra:

# for number in range(300, 600):
#     my_pets_list.apppend(number)
#aqui le decimos que al final de la lista agregue los numeros de 300 a 600



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''




'''Insertar datos con insert'''
#Aqui utilizamos el insert para agregar datos a un indice especifico

courses_list = [
	'Computers',
	'Algorithms',
	'Python',
	'Web Development',
]

courses_list.insert(2, 'Databases')
print(courses_list)

#R/
#['Computers', 'Algorithms', 'Databases', 'Python', 'Web Development']



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''Metodo extend'''
#También podemos usar el método extend para agregar elementos de una lista a otra y unirlas:

first_list = [
	'A',
	'B',
	'C',
]

second_list = [
	'D',
	'E',
	'F',
]

first_list.extend(second_list)
print(first_list)

#R/ ['A', 'B', 'C', 'D', 'E', 'F']

#extra codigo:
first_list.append(second_list)
print(first_list)

#Aqui lo que hace es basicamente meter una lista dentro de otra, asi que no es tan correcto, se ve mal



'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''



'''Eliminar datos'''

milky_way_planets = [
	'Mercury',
	'Venus',
	'Earth',
	'Mars',
	'Pluto',
	'Jupiter',
	'Saturn',
	'Uranus',
	'Neptune',
]

#extra codigo: esto lo usamos para averiguar el indice del elemento que queremos borrar
# pluto_index = 0
# for index, planet in enumerate(milky_way_planets):
#     if planet == 'Pluto':
#         print(index)
#         pluto_index = index
# deleted_item = milky_way_planets.pop(pluto_index)


deleted_item = milky_way_planets.pop(4)
print(milky_way_planets)
print(f'Deleted item: {deleted_item}')



#extra codigo:
# milky_way_planets.pop(4)
# print(milky_way_planets)
#esto es como una forma directa pero arriba guarda el elemento eliminado y lo guarda en una variable 
#para hacer con ese valor despues algo

