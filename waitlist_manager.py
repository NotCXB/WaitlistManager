# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        new_node = self.head is None:
        new_node.next = self

        print("Current waitlist:")
        current = self.head

        while current is not None:
            print(f"- {current.name}")
            current = current.next

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        return f" {name} has been added to the end of the waitlist."

    def remove(self, name):
        current = self.head
        previous = None

        while current is not None:
            if current.name == name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return f"{name} has been removed from the waitlist."
            previous = current
            current = current.next

        return f"{name} is not in the waitlist."

    
    


def waitlist_generator():
    # Create a new linked list instance
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
