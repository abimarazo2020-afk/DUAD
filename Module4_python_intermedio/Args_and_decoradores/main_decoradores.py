'''                              DECORADORES                        '''


'''Para crear decoradores usan la siguiente sintaxis:'''


def decorator_name(func): #fun es la funcion decorada 
    def wrapper(parameters):
        # Logica extra
        func(parameters) # Llamada a la funcion decorada
				# Logica extra

    return wrapper
    
    
'''Por ejemplo, digamos que tenemos varias funciones 
que se pueden ejecutar solo por usuarios con el rol de administrador:'''

class User:
    role: str

    def __init__(self, role):
        self.role = role


def create_product(user, product_name):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )

    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


def create_product_category(user, product_category_name):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )

    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


def modify_order(user, order_id):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )

    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")
    
#correcto
my_user = User("Admin")
modify_order(my_user, 4)

#R/ Order 4 modified!

#incorrecto
my_user = User("Customer")
modify_order(my_user, 4)

#R/ ValueError: You are not allowed to run this function. You are not an admin


'''
Tenemos lógica repetida en el de arriba que rompe con el principio DRY.
Una solución a esto sería convertir esa lógica de verificación en una función:'''



class User:
    role: str

    def __init__(self, role):
        self.role = role


def check_if_user_is_admin(user):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )


def create_product(user, product_name):
    check_if_user_is_admin(user)

    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


def create_product_category(user, product_category_name):
    check_if_user_is_admin(user)

    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


def modify_order(user, order_id):
    check_if_user_is_admin(user)

    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")
    
    
    
'''Sin embargo, tenemos que estarle pasando el user a la función, y también se vuelve algo repetitivo.
La solución más elegante y recomendada en estos casos donde hay que validar algo de manera repetitiva 
antes de la lógica de la función es crear un decorador:'''


class User:
    role: str

    def __init__(self, role):
        self.role = role


def admin_only(func):
    def wrapper(user, *args):
        if user.role != "Admin":
            raise ValueError(
                "You are not allowed to run this function. You are not an admin"
            )
        func(user, args)

    return wrapper


@admin_only
def create_product(user, product_name):
    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


@admin_only
def create_product_category(user, product_category_name):
    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


@admin_only
def modify_order(user, order_id):
    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")
    
    
    
'''                                 Property decorador                    '''

class Student:
    spanish_score: int
    english_score: int

    def __init__(self, spanish_score, english_score):
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.average_score = (spanish_score + english_score) / 2


student_ian = Student(80, 80)
print(f"Average score: {student_ian.average_score}")

student_ian.spanish_score = 50
print(f"Average score: {student_ian.average_score}")

#R/ incorrecto
# Average score: 80.0
# Average score: 80.0

# Como podemos observar, el average sigue siendo 80 a pesar de que su nota de español cambió.
# Esto es incorrecto, así que deberíamos calcular el average de nuevo cada vez que cambia una nota, lo cual tampoco seria ideal.
# O hacerlo un property que se calcule cada vez que se necesite.



class Student:
    spanish_score: int
    english_score: int

    def __init__(self, spanish_score, english_score):
        self.spanish_score = spanish_score
        self.english_score = english_score

    @property #Aqui es donde sucede la magia, ejecuta este metodo y lo hace dinamico
    def average_score(self):
        return (self.spanish_score + self.english_score) / 2


student_ian = Student(80, 80)
print(f"Average score: {student_ian.average_score}")

student_ian.spanish_score = 50
print(f"Average score: {student_ian.average_score}")

#R/ CORRECTO
# Average score: 80.0
# Average score: 65.0



'''                           Decorador class method                       '''

'''El decorator @classmethod permite crear métodos en una clase que pueden ser llamados sin necesidad de instanciar la misma.
En otros lenguajes se les suele conocer como static methods.
Es decir que se pueden llamar directamente usando el nombre de la clase y el método sin tener que crear un objeto de la clase.
Esto podemos usarlo para funcionalidades que son parte de la clase, pero no necesariamente de un objeto especifico de esa clase.
Por ejemplo, se suele usar para crear métodos que ayuden a crear instancias de la clase:'''


from datetime import datetime


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class User:
    def __init__(self, email, password, person):
        self.email = email
        self.password = password
        self.person = person


my_person = Person("Sarah", "Connor")
my_user = User("sconor@gmail.com", "321", my_person)

print("User: ", vars(my_user))
print("Person: ", vars(my_user.person))



from datetime import datetime


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class User:
    def __init__(self, email, password, person):
        self.email = email
        self.password = password
        self.person = person

    @classmethod
    def create_user(cls, first_name, last_name, email, password):
        person = Person(first_name, last_name)
        return cls(email, password, person)


my_user = User.create_user("Sarah", "Connor", "sconor@gmail.com", "321")

print("User: ", vars(my_user))
print("Person: ", vars(my_user.person))


#r/
# User: {'email': 'sconor@gmail.com', 'password': '321', 'person': <main.Person object at 0x104a02710>}
# Person: {'first_name': 'Sarah', 'last_name': 'Connor'}

# En este caso, el User necesita también una instancia de Person.
# Entonces tiene más sentido crear el Person y el User desde un método, y no desde el constructor del User (ya que el Person es una clase distinta).
# Y este método no necesita un User previamente creado, así que tiene más sentido hacerlo un classmethod.