class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.next= None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
  
    def append(self,key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
    
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def view(self):
        if self.head is None:
            print("Linked ia empty")
        else:
            current = self.head
            while current is not None:
                print(f"Key: {current.key}")
                current = current.next

LL=LinkedList()
LL.append(10)
LL.append(20)
LL.view()