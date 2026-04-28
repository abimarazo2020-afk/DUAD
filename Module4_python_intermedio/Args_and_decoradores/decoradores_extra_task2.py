'''EJERCICIO#2
Cree un decorador @requires_login que:
Verifique si la variable global user_logged_in es True
Si no lo es, debe lanzar una excepción "Usuario no autenticado"
Si lo es, la función decorada se ejecuta normalmente
Ejemplo:
Entrada:
user_logged_in = False

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")
    
'''

user_logged_in = False

def requires_login(fun): #funcion que mas adelante va a ser approved_profile
    def wrapper(*args, **kwargs):
        print('Parameters: ', args, kwargs)
        if user_logged_in == False:
            raise PermissionError("Access denied, Try again.")
            
        else:
            print("access granted")
            
        return fun(*args, **kwargs)
        
    return wrapper
    
@requires_login
def profile_access(name):
    print(f"{name}'s profile approved")