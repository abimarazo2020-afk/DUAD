'''EJERICIO#2
Cree un decorador que se encargue de revisar si todos los parámetros
de la función que decore son números, y arroje una excepción de no ser así.
'''
def decorador(fun):
    def wrapper(*args, **kwargs):  # args parametros normales, kwargs parametros con nombre
        for value in args:
            if not isinstance(value, int):
                raise TypeError("Only numbers allowed.")
                
        for value in kwargs.values():
            if not isinstance(value, int):
                raise TypeError("Only numbers allowed.")
                
        
        return fun(*args, **kwargs)
        
    return wrapper

@decorador
def create_user(badge, name):
    return f"{badge}, {name}"
    
# 👉 Python hace esto internamente:
# create_user = decorador(create_user)
#Ahora create_user ES wrapper
    
create_user(65797, 'Abigail')

