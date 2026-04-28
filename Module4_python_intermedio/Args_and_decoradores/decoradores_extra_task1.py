'''EJERCICIO#1
Cree una función que imprima “Hola, [nombre]” dos veces:
Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, 
con los mismos argumentos.

Ejemplo:
Salida:

Copiar
"Hola, Jeanca"
"Hola, Jeanca"

'''

def repeat_twice(fun):
    def wrapper(*args, **kwargs):
        print('Parameters:', args, kwargs)
        
        fun(*args, **kwargs) #aqui no se pone return porque si no la sig linea no corre 
        return fun(*args, **kwargs) 
        
    return wrapper

@repeat_twice
def hola_print(name):
    print(f'Hello, {name}')
    
    
hola_print('Abigail')
    
