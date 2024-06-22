class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def add_Node(self,data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.ref is not None:
                current = current.ref
            current.ref = new_node

    def delete(self,key):
        current = self.head
        if current is not None:
            if current.data == key:
                  current  = current.ref
                  current = None
                  return
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.ref
            if current is None:
                print("Node not found in the list")
            return

        # Unlink the node from the linked list
        prev.ref = current.ref

        current = None 
    def view(self):
        if self.head is None:
            print("Linked list is null")
        else:
            current = self.head
            while current:
                print(f" {current.data}=>",end="")
                current = current.ref
            print(None)
ll = LinkedList()
ll.add_Node(10)
ll.add_Node(20)
ll.add_Node(40)
ll.add_Node(50)
ll.delete(40)
ll.view()
    