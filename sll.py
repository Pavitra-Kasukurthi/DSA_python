class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


class SLL():
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def print_sll(self):
        if self.head==None:
            print("Their is no data")
        curr=self.head
        while curr:
            print(curr.data, end=" -> ")
            curr=curr.next
        print("None")
l=SLL()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)

l.print_sll()
        
        
        