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


    def add_front(self, value):
        #time: O(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def add_back(self, value):
        #time: O(n)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next - Node(value)


    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.next)
            current_node = current_node.next


ll = LinkedList()
ll.head = Node(1)
ll.next.next = Node(2)
ll.next.next.next = Node(3)

