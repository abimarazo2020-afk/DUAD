'''EJERICICIO#1
Cree una estructura de objetos que asemeje un Stack.
Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
Debe incluir un método para hacer print de toda la estructura.
No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
'''


class Node: #la clase nodo es como la cajita donde guardamos el valor y la referencia al siguiente nodo.
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Stack: #la clase stack ya llevaria toda la estructura con los metodos.
    
    def __init__(self, head=None): # Normalmente un stack empieza vacío. por eso NONE
        self.head = head 
        
    def push(self, data):
        new = Node(data) #Aquí creas un nodo nuevo. asi que valor que ingresamos seria el primer node y asi sucesivamente 
        
        #si la cabeza esta vacia:
        if not self.head: #¿head es None?
            self.head = new #aqui new seria el head del stack, ejemplo: head -> [10] -> None
            return 
            
        new.next = self.head #aqui el sig de 20 es 10, el 10 seria el next del 20 
        self.head = new #aqui asignamos el  nuevo head.
     
    def pop(self):
        
        if not self.head:
            return None
         
        temp = self.head #guardamos el head actual porque ese va a ser eliminado
        self.head = self.head.next #asugnamos nuevo head
        return temp.data #retornamos el valor que sale del stack
        
    def print_estructure(self):
        temp_head = self.head #variable temporarl para recorrer
        while temp_head:  #validamos que exista head
            print(temp_head.data, end = "-")  
            temp_head = temp_head.next #apuntamos al sig.
        print('None')
        
        

#crear stack vacio
stack = Stack()

#agregar elementos
stack.push(10)
stack.push(20)
stack.push(30)

#imprimir estructura
stack.print_estructure()


#eliminar elemento
print("Elemento eliminado:", stack.pop())

# imprimir nuevamente
stack.print_estructure()



#NOTAS:
        
#Creas una variable temporal para recorrer.

# Eso es importante porque:

# NO quieres mover el self.head real
# solo recorrer la estructura

