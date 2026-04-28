'''Esto lo podemos lograr agregando 
un asterisco * a la izquierda de uno de los parámetros de nuestra función.
El standard para este tipo de parámetros es llamarles args (arguments).
Los args van a venir siempre en formato de lista, así que podemos iterarlos.'''


'''                                     ARGS                                '''

def my_function_with_infinite_params(*args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")


my_function_with_infinite_params(
    2, 5, 6, 3, 6, 5, 6
)

#R/

# Arg 0: 2
# Arg 1: 5
# Arg 2: 6
# Arg 3: 3
# Arg 4: 6
# Arg 5: 5
# Arg 6: 6


'''También podemos combinarlos con otros parámetros.'''


def my_function_with_infinite_params(my_other_param, *args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"My other param: {my_other_param}")


my_function_with_infinite_params(10, 2, 5, 6, 3, 6, 5, 6) #Aqui el numero 10 es el primer parametro


#R/

# Arg 0: 2
# Arg 1: 5
# Arg 2: 6
# Arg 3: 3
# Arg 4: 6
# Arg 5: 5
# Arg 6: 6
# My other param: 10


'''
Sin embargo, los parámetros que no sean parte de los args y vayan después 
de estos hay que definirlos con su nombre al llamar a la función 
(sino, Python no sabrá cómo diferenciarlos).'''


def my_function_with_infinite_params(*args, my_other_param):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"My other param: {my_other_param}")


my_function_with_infinite_params(2, 5, 6, 3, 6, 5, 6, my_other_param=10) #lo definimos aqui 

#R/
# Arg 0: 2
# Arg 1: 5
# Arg 2: 6
# Arg 3: 3
# Arg 4: 6
# Arg 5: 5
# Arg 6: 6
# My other param: 10



'''                                  KWARGS                                                '''


'''
Keyword Arguments.
Así mismo, también podemos hacer que nuestra función acepte parámetros con nombre infinitos.
Esto lo podemos lograr agregando dos asteriscos ** a la izquierda de uno de los parámetros de nuestra función.
El standard para este tipo de parámetros es llamarlos kwargs (keyword arguments).
Los kwargs van a venir siempre en formato de diccionario (con los keys siendo los nombres que les demos al llamar la función).
Los kwargs siempre deben de ir de ultimo.'''

def my_function_with_infinite_named_params(parameter_1, **kwargs):
    print(f"Parameter 1: {parameter_1}")
    print(f"Kwargs: {kwargs}")


my_function_with_infinite_named_params("Hello", my_other_parameter="World", whatever=6)

#R/
# Parameter 1: Hello
# Kwargs: {'my_other_parameter': 'World', 'whatever': 6}



'''Los parámetros normales, args y kwargs se pueden combinar y usar en conjunto.'''


def my_function(first_parameter, *args, **kwargs):
    print(f"First parameter: {first_parameter}")
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"Kwargs: {kwargs}")


my_function("First value", 1, 2, 3, 4, my_other_parameter="World", whatever=6)



#R/

# First parameter: First value
# Arg 0: 1
# Arg 1: 2
# Arg 2: 3
# Arg 3: 4
# Kwargs: {'my_other_parameter': 'World', 'whatever': 6}

