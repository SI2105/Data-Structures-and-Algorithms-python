class DNode: #Doubly Linked List Node with the required variables.
    def __init__(self, data, next, prev):
        self.data = data # Keeps the value of the node
        self.next = next # Stores pointer to next DNode object in DLinkedList
        self.prev = prev # Stores pointer to previous DNode object in DLinkedList
        

class DLinkedList: #Doubly Linked List class
    def __init__(self):
        self.head = None # Stores reference to the head DNode in the DLinkedList
        self.tail = None # Stores reference to the tail DNode in the DLinkedList
        self.length = 0  # Stores length of DLinkedList

