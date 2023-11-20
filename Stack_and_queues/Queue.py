from Linked-List import linked_list

class Queue:
    def __init__(self):
        self.data = linked_list()
    
    def enqueue(self, value):
        """Add a value to the queue"""
        # LL O(1)
        self.data.add_back(value)

    def dequeue(self):
        """"Remove value from the queue"""
        # LL O(1)
        return self.data.delete_front()

