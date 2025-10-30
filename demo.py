# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # store the data
        self.next = None  # pointer to the next node


# LinkedList class manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # initially, the list is empty

    # Method to insert a new node at the end
    def append(self, data):
        new_node = Node(data)

        # if the list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # otherwise, traverse to the end and append
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to print all nodes in the list
    def print_list(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# -------------------------------
# Example usage
# -------------------------------
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Linked List:")
ll.print_list()
