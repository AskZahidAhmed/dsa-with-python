class Node:
    def __init__(self, data = None):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n
    
    def insert(self, data):
        node = Node(data)
        self.next = self.head
        self.head = node
        self.n += 1

LL = LinkedList()

LL.insert(1)
LL.insert(5)
LL.insert(10)
print(LL.__len__())