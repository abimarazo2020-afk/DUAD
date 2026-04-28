'''Cree una clase Product con:
Nombre, precio y cantidad
Cree una clase Inventory que:
Guarde productos en una lista
Tenga métodos para:
Agregar un producto
Mostrar todos los productos
Calcular el valor total del inventario'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    
class Inventory:
    def __init__(self): 
        self.product_list = [] #ponemos la lista como atributo para que no quede local y exista en toda la clase
    
    def save_products(self, product):
        if product not in self.product_list:
            self.product_list.append(product)
            
    def show_all_products(self):
        for product in self.product_list:
            print(f"product name: {product.name}, price: {product.price}, quantity: {product.quantity}")
            #aqui product va por delante porque se habla de cada producto individual por eso no es self.
            
    def get_total_inventory(self):
        sum = 0
        for product in self.product_list:
            sum += product.quantity * product.price
        return sum
        
def main():

    product_1 = Product('Butter', 1300, 2)
    product_2 = Product('Coffe', 5000, 1)
    product_3 = Product('Banana', 75, 5)

    inventory_1 = Inventory()
    inventory_1.save_products(product_1)
    inventory_1.save_products(product_2)
    inventory_1.save_products(product_3)

    inventory_1.show_all_products()
    print(inventory_1.get_total_inventory())
    
if __name__ == "__main__":
    main()