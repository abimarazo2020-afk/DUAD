'''Lista doblemente enlazada
Requisitos:
Cada nodo debe tener referencia al siguiente y al anterior
Métodos:
append(data): Agrega al final
prepend(data): Agrega al inicio
delete(data): Elimina el primer nodo con ese valor
print_forward() y print_backward(): Imprime en ambas direcciones
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def append(self, data):
        node_1 = Node(data)
        
        if self.tail is None: #si no hay cola, pues se asigna a los dos 
            self.head = node_1
            self.tail = node_1
            
        else: #si ya hay algo:
            node_1.prev = self.tail #el anterior del nuevo node va a ser el tail
            self.tail.next = node_1 #y el siguiente que va a ocupar tail es el que ingresamos
            
            self.tail = node_1
            
            ##  <<<<< logica: >>>>>> 
            #El nuevo nodo apunta hacia atrás al tail actual
            #El tail actual apunta hacia adelante al nuevo nodo
            #El nuevo nodo se convierte en el nuevo tail
            
            
    def prepend(self, data):
        node_2 = Node(data)
        
        if self.head is None:
            self.head = node_2
            self.tail = node_2
            
        else:
            node_2.next = self.head
            self.head.prev = node_2
            
            self.head = node_2
            
    
    def delete(self, data):

        current = self.head

        # recorrer la lista
        while current:

            # encontramos el nodo
            if current.data == data:

                # caso 1: solo hay un nodo
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                # caso 2: borrar head
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                # caso 3: borrar tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # caso 4: borrar en medio
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return

            current = current.next
                

    def print_forward(self):

        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


    def print_backward(self):

        current = self.tail

        while current:
            print(current.data, end=" ")
            current = current.prev

        print()
        
        
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

dll.print_forward()
dll.print_backward()

dll.delete(20)

dll.print_forward()
dll.print_backward()