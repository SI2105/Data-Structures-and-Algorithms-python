class DNode: #Doubly Linked List Node with the required variables.
    def __init__(self, data, next, prev):
        self.data = data # Keeps the value of the node
        self.next = next # Stores pointer to next DNode object in DLinkedList
        self.prev = prev # Stores pointer to previous DNode object in DLinkedList
        
    def __str__(self):
        return str(self.data)
        
class DLinkedList: #Doubly Linked List class
    def __init__(self):
        self.head = None # Stores reference to the head DNode in the DLinkedList
        self.tail = None # Stores reference to the tail DNode in the DLinkedList
        self.length = 0  # Stores length of DLinkedList
    def append(self, data):
        self.length += 1 #Increases the size of the DLinkedList
        if self.head == None: #Case for when DLinkedList is empty
            self.head = DNode(data,None,None) #New node with data is made he head
            self.tail = self.head #Tail points to the head as there is only one item
        else: #The DLinkendList is not empty
            new_node = DNode(data, None, self.tail) # New Node with the data, next pointer to none and prev pointer to tail is created.
            self.tail.next = new_node # Tails next pointer points to the new_node
            self.tail = new_node #the tail now points to new node
L = DLinkedList()

L.append(2)
print(L.head)
print(L.tail)
L.append(3)
print(L.head)
print(L.tail)