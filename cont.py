class ContactBook:
    def __init__(self):
        self.contacts = {}  # Initialize an empty dictionary to store contacts

    def add_contact(self, name, phone_number, email, address):
        """Add a new contact."""
        self.contacts[name] = {'phone': phone_number, 'email': email, 'address': address}
        print(f"Contact '{name}' added successfully!")

    def view_contact(self, name):
        """View contact details."""
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Contact Details for '{name}':")
            print(f"Phone Number: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone_number, email, address):
        """Update contact details."""
        if name in self.contacts:
            self.contacts[name] = {'phone': phone_number, 'email': email, 'address': address}
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            name = input("Enter contact name: ")
            contact_book.view_contact(name)
        elif choice == '3':
            name = input("Enter contact name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone, email, address)
        elif choice == '4':
            name = input("Enter contact name: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
