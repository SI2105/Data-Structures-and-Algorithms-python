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

    def __str__(self): # Prints the Doubly Linked List both reversed and
        # normal to make sure the next and prev pointer are both correct
        st = ""
        ptr = self.head
        while ptr != None:
            st = st + str(ptr.data)
            st = st+" -> "
            ptr = ptr.next
        st += "None, and reversed: "
        ptr = self.tail
        while ptr != None:
            st = st + str(ptr.data)
            st = st+" -> "
            ptr = ptr.prev
        return st+"None"

    def append(self, data):
        self.length += 1 #Increases the size of the DLinkedList
        if self.head == None: #Case for when DLinkedList is empty
            self.head = DNode(data,None,None) #New node with data is made he head
            self.tail = self.head #Tail points to the head as there is only one item
        else: #The DLinkendList is not empty
            new_node = DNode(data, None, self.tail) # New Node with the data, next pointer to none and prev pointer to tail is created.
            self.tail.next = new_node # Tails next pointer points to the new_node
            self.tail = new_node #the tail now points to new node

    def search(self, d): # Searched the liked list by value
        i = 0
        ptr = self.head
        while ptr != None: # Loop until end of list reached
            if ptr.data == d:
                return i # Return the index if the data is the value you are looking for
            ptr = ptr.next # Move the pointer foward
            i += 1 # Update Counter
        return -1 # Returns -1 if the value d does not exist
    
    def remove(self, i): # Removes item in the given index i
        if self.head == None: #Case for Empty List
            return None
      
        if i == 0: # Case to remove the first element
            val = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return val
        ptr = self.head
        if i == self.length - 1: # Case to remove the last element in the list
            self.tail = self.tail.prev
            self.tail.next = None
        while ptr.next != None: # Otherwise loops until the index is 1
            if i == 1: # At which point the item ptr.next is deleted
                val = ptr.next.data #Value to remove is stored
                ptr.next = ptr.next.next # Pointer to next is updated so it skips one element(the one for removal)
                ptr.next.prev = ptr
                self.length -= 1
                return val
            ptr = ptr.next
            i -= 1
    def insert(self, i, d): # Inserts value d at index i
        if self.head == None : # Deals with case if the DLinked List Empty
            self.head = DNode(d,self.head,None)
            self.tail = self.head
        elif i == 0:
            newnode = DNode(d,self.head,None)
            self.head.prev = newnode
            self.head = newnode
            
        else: 
            ptr = self.head
            while i>1 and ptr.next != None: #Loops until end of list is reached or the index before i is reached.
                ptr = ptr.next
                i -= 1
            newnode = DNode(d,ptr.next,ptr)
            if ptr.next is not None: #If there is currently a node in i.
                ptr.next.prev = newnode
            ptr.next = newnode
        if newnode.next is None: #If there is no node after the newnode.
                self.tail = newnode
        self.length += 1



