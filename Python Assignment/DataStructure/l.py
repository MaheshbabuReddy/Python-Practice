class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None 

    def new_list(self):
        input_list = list(map(int, input("Enter the numbers separated by spaces: ").split()))
        self.append(input_list)
        print("List created: ", input_list)

    def append(self, input_list):
        for data in input_list:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_node

    def view(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(f"{current.data} -> ", end="")
                current = current.next
            print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

        # Printing the reversed list
        current = self.head
        while current is not None:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

  
ll = LinkedList()
ll.new_list()
ll.view()
ll.reverse()
ll.reverse2()