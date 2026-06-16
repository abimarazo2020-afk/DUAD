'''EJERCICIO#3
Cree una estructura de objetos que asemeje un Binary Tree.
Debe incluir un método para hacer print de toda la estructura.
No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.'''


class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None  #hijo del node
        self.right = None #hijo del node
        
        
    def print_tree(self):
    
        print(self.data)
        
        if self.left:
            self.left.print_tree()
        
        if self.right:
            self.right.print_tree()
        
        
#creacion de nodos
a = Node(10)
b = Node(5)
c = Node(20)

a.left = b   #el hijo de a izq es 5, no pocia el numero, concecta objectos 
a.right = c  #el hijo de a derecho es 20
    
    
print(a.data)
print(a.left.data)
print(a.right.data)

a.print_tree() #imprime el arbol entero.


