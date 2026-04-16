'''Cree una clase abstracta User con los siguientes métodos abstractos:
get_role()
has_permission(permission)
Luego cree dos clases que hereden de ella:
AdminUser
RegularUser
Cada una debe implementar los métodos
Por ejemplo:
AdminUser siempre tiene permisos
RegularUser solo tiene permisos limitados ("read", por ejemplo)'''

from abc import ABC, abstractmethod #IMPORTANTE

#clase padre
class User(ABC):
    
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass
    
#clase hija 
class AdminUser(User):
    def __init__(self):
            pass
    
    def get_role(self): 
        return "admin"
        
    def has_permission(self, permission):
        return True #True porque adminuser siempre tiene permisos 
        
         
#clase hija 
class RegularUser(User):
    def __init__(self, permissions):
        self.permissions = permissions
        
        
    def get_role(self):
        return "regular"
        
    def has_permission(self, permission):
        if permission in self.permissions:
            return True
        else:
            return False
        
#SI NO GUARDAMOS LOS PERMISOS EN INIT
#  No sabe qué permisos tiene
#  No puede comparar nada en has_permission
#  No puede responder correctamente
     
       
#CREACION DE OBJECTOS

user_1 = AdminUser()

user_2 = RegularUser(['read', 'write'])

print('user_1 role: ', user_1.get_role())
print('user_1 can delete? ', user_1.has_permission("delete")) #recordemos que has_permission tiene parametro

print('user_2 role: ', user_2.get_role())
print('user_2 can read? ', user_2.has_permission("read")) #recordemos que has_permission tiene parametro
print('user_2 can delete? ', user_2.has_permission("delete")) #recordemos que has_permission tiene parametro