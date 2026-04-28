'''EJERCICIO#3

Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos
Ejemplo:
Entrada:
multiply(3, 4)

"func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
"Resultado 12"

'''

from datetime import datetime


def log_call(fun):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args) #aqui hacemos esta conversion de tupla a strings, abajo la explicacion.
        now = datetime.now()
        
        result = fun(*args, **kwargs)
        
        print(f"func:{fun.__name__} - args: {args_str} - [{now}] - result: {result}")
        print(f'Resultado {result}')
        
        return result
           
    return wrapper
    
    
def validate_numbers(fun):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be numeric")
                
        return fun(*args, **kwargs) 
        
    return wrapper
    
    
@log_call
@validate_numbers
def multiply(x, y):
    result = x * y
    return result
        
        
multiply(10, 5)

#1. si llamamos multiply(3, 4) dentro del wrapper: args = (3, 4) > tupla
#2. for a in args recorre los valores de la tupla
#3. str(a) Convierte cada número en texto: "3" , "4"
#4. (str(a) for a in args) Esto es un generator expression (como una lista pero sin corchetes). produce: "3", "4"
#5. ", ".join(...) Esto une esos strings con ", " entre ellos: 
#6. args_str es una variable nueva, totalmente independiente de args. args sigue siendo una tupla y args_str es un string (texto)
#7. fun.__name__ devuelve el nombre de la función como texto (string)



