'''Cree una estructura que represente una cola básica (Queue) con objetos enlazados
Restricción:
no usar list, dict, tuple, collections

enqueue(data): agrega un nodo al final

dequeue(): elimina y retorna el nodo del inicio


print_all(): imprime todos los elementos de la cola en orden'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        

class LinkedList:
    def __init__(self, head):
        self.head = None
    
    def print_structure(self):
        temp = self.head
        
        while temp is not None:
            print(temp.data)
            temp = temp.next
        
class Queue(LinkedList):

    def enqueue(self, new_node):

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        
    def dequeue(self):
        if self.head is None:
            return None
            
        removed_node = self.head
        self.head = self.head.next 
        
        removed_node.next = None
        
        return removed_node
        
queue = Queue()


queue.enqueue(Node(10))
queue.enqueue(Node(20))
queue.enqueue(Node(30))

queue.print_all()

removed = queue.dequeue()

print("Removed:", removed.data)