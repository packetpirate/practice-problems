# Supporting class for testing purposes.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# This function will reverse a linked list.
# ie: Given the list A -> B -> C, the list should be modified to be C -> B -> A
def reverse(head):
    if head == None: return None
    current = head
    newHead = reverseHelp(current, None)
    return newHead
    
def reverseHelp(current, last):
    if current.next == None:
        current.next = last
        return current
    else:
        h = reverseHelp(current.next, current)
        current.next = last
        return h

# This will print the linked list in order.
def printList(head):
    current = head
    s = ""
    while current != None:
        s += str(current.data)
        if current.next != None: s += " -> "
        current = current.next
    print(s)

# Create the linked list A -> B -> C
L = Node('A')
L.next = Node('B')
L.next.next = Node('C')

printList(L)

R = reverse(L)

print()
printList(R)
