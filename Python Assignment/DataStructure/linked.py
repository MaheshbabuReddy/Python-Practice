class Node:
    def __init__(self , key) -> None:
        self.key = key
        self. ref = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self,arr):
        for data in arr:
            New_Node = Node(data)
            if self.head is None:
                    self.head = New_Node
            else:
                current = self.head
                while current.ref is not None:
                    current = current.ref
                current.ref = New_Node
    def delete(self, key):
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return
        current = self.head
        while current.ref is not None:
            if current.ref.key == key:
                current.ref = current.ref.ref
                return
            current = current.ref
        
        print(f"Node with key {key} not found.")

    def view(self):
        if self.head is None:
            print("LL is Null")
        else:
            current = self.head
            while current is not None:
                print(f"{current.key}--->",end="")
                current = current.ref
            print("None")
    

arr = [1,2,7,12,3,1]
ll=LinkedList()
ll.addNode(arr)
ll.delete(1)
ll.view()

