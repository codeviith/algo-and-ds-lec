class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    def __repr__(self) -> str:
        return f"<Node {self.data}>"

### normal variable assignment:
# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next = b
# b.next = c


### using linked list:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    #time: O(1)
    def add_front(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node


    def add_back(self, value):
        #time: O(1)
        new_node = Node(value)

        if self.head is None: # This is to check to see if our list s empty.
            self.add_front(value)
        else:
            self.tail.next = new_node
            self.tail = new_node

        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node


        #time: O(n)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next - Node(value)

    #time: O(1)
    def delete_front(self):
        value = self.head.data

        if self.head is not None:
            self.head = self.head.next ## This is the actual delete code --> severing the link at the front
        elif self.head.next is None:
            self.head = None
            self.tail = None

        return value
        
        
        # value = self.head.data
        # self.head = self.head.next ## This is the actual delete code --> severing the link at the front


    #time: O(n)
    def delete_back(self):
        current = self.head
        
        if self.head.next is None: ## This is to check for the special case where there is only one node.
                                   ## self.head.next means that there is only one node
            value = self.head.data
            self.head = None

            return value
        
        while current.next.next is not None:
            current = current.next
        value = current.next.data
        self.tail = current
        current.next = None ## this is the actual delete code --> severing the link at the end
        
        return value


    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.next)
            current_node = current_node.next


ll = LinkedList()
ll.head = Node(1)
ll.next.next = Node(2)
ll.next.next.next = Node(3)

