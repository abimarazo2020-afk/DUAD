'''EJERCICIO#1
Cree un decorador que haga print de los parámetros y retorno de la función que decore.'''


def decorador(fun):
    def wrapper(*args, **kwargs): #porque no se sabe cuantos parametros son
        print('Parametros:', args, kwargs)
        
        result = fun(*args, **kwargs) #aqui llamamos a la funcion original y guardamos lo que devuelve
        
        print('Result:', result)
        
        return result
        
    return wrapper
        
        
# fun = la función original (print_my_name)
# La ejecutas con los mismos parámetros
# Guardas lo que devuelve en result

@decorador
def print_my_name(name, last_name): #wrapper tiene que recibir estos parametros
    return f'{name} {last_name}'
    
print_my_name('Abigail', 'Azofeifa') #En realidad estás llamando al wrapper