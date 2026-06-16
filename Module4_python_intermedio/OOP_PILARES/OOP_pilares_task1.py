'''Cree una clase de BankAccount que:
Tenga un atributo de balance.
Tenga un método para ingresar dinero.
Tengo un método para retirar dinero.
Cree otra clase que herede de esta llamada SavingsAccount que:
Tenga un atributo de min_balance que se pueda asignar al crearla.
Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.'''


class BankAccount:  #CLASE PADRE 
    def __init__(self, balance):
        self.balance = balance
        
    
    def add_balance(self, amount):
        self.balance += amount
        
        
    def withdraw_balance(self, amount):
        self.balance -= amount
        

    

class SavingsAccount(BankAccount): #CLASE HIJA, HEREDA LA PADRE
    def __init__(self, balance, min_balance):
        self.min_balance = min_balance
        super().__init__(balance) #llama al constructor del padre.
       
    
    def withdraw_balance(self, amount):
      if (self.balance - amount) < self.min_balance:
        raise ValueError('You cant withdraw the money')
    
    # si pasa la validación
      self.balance -= amount  #Esto hace la resta.

    #Creacion de objectos:
    
def main():
    
    account_1 = BankAccount(100) #asignamos el balance a la cuenta
    account_2 = BankAccount(200) #asignamos el balance a la cuenta
    account_3 = BankAccount(300) #asignamos el balance a la cuenta
    
    account_4 = SavingsAccount(200, 50) #aqui el balance y luego el minimo
    
    account_1.withdraw_balance(30) #AQUI SE ASIGNA AMOUNT
    account_2.add_balance(100) #AQUI SE ASIGNA AMOUNT
    
if __name__ == "__main__":
    main()