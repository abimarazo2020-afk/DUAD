'''Cree una clase de User que:
Tenga un atributo de date_of_birth.
Tenga un property de age.
Luego cree un decorador para funciones que acepten un User como parámetro 
que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.'''

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth  
        
        
    @property  #se usa property porque age es dinamico y para obtener la edad ocupamos compararla con el dia actual.
    def age(self):
        today = date.today()   #nos da dia, mes, ano. /today() es una funcion de python. / today es la variable que creamos, se obtiene automaticamente, no se ocupa como parametro 
        age =   today.year - self.date_of_birth.year      #no se pide como parametro porque los calculamos aqui mismo, “de la variable today, dame su atributo year”
    
        if(today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
            
        return age
            
                 
# `date.today()` | función (se ejecuta) 
# `today.year`   | atributo (se accede) 


def decorador(fun):
    def wrapper(*args, **kwargs): #args es una tupla, args se convierte en user 
        print('Age: ', args, kwargs)
        
        if args[0].age < 18:
            raise ValueError('You are not of legal age.')
            
        result = fun(*args, **kwargs)
        print(f'You have the enough age, {result}')
        return result
            
    return wrapper
        
@decorador   
def get_age(user):
    return f'{user}'
        
    
user_1 = User(date(2000, 10, 12))
get_age(user_1)   #llama a wrapper y la tupla recibe (user, )



