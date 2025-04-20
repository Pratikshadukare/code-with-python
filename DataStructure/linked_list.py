class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# creating the NODE 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

#conncetiong the nodes

node1.next = node2
node2.next = node3

# print linked_list

head = node1

current = node1

while current.next is not None:
    print(current.data, end="->")
    current = current.next

print(None)

