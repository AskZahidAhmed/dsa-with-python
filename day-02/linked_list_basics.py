class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # The value inside this node
        self.next = next      # A pointer to the next node

# Step 1: Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

print("Step 1: Creating nodes...")
print(node1.val, node2.val, node3.val)

# Step 2: Link the nodes together
node1.next = node2
node2.next = node3

print("Step 2: Linking nodes...")
print("node1.next:", node1.next.val)
print("node2.next:", node2.next.val)

# Step 3: Start from the head (first node)
print("Step 3: Traversing the list")
head = node1

# Step 4: Traverse and print each node's value
print("Step 4: Traversing the list")
while head:
    print(head.val, end=" -> ")
    head = head.next


