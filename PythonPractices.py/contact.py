class Contact:
    def __init__(self):
        self.contacts = {}

    def add(self, name, ph_num):
        self.contacts[name] = ph_num
        print("Contact added:", name, ph_num)

    def search(self, search_name):
        if search_name in self.contacts:
            print("Contact found:", search_name, self.contacts[search_name])
        else:
            print("Contact not found for", search_name)

    def remove(self, search_name):
        if search_name in self.contacts:
            del self.contacts[search_name]
            print("Contact removed for", search_name)
        else:
            print("Contact not found for", search_name)

if __name__ == '__main__':
    contact = Contact()

    while True:
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            ph_num = input("Enter phone number: ")
            contact.add(name, ph_num)

        elif choice == 2:
            search_name = input("Enter name to remove: ")
            contact.remove(search_name)

        elif choice == 3:
            search_name = input("Enter name to search: ")
            contact.search(search_name)

        elif choice == 4:
            print("Exiting the contact management system.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")




                


        
