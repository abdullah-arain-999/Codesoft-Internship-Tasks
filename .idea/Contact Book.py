print(('---------------------------------------'))
print(('            CONTACT-MANAGER            '))
print(('---------------------------------------'))

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for idx, contact in enumerate(self.contacts):
            print(f"Contact {idx + 1}")
            print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone_number]
        return results

    def update_contact(self, contact, name=None, phone_number=None, email=None, address=None):
        if name:
            contact.name = name
        if phone_number:
            contact.phone_number = phone_number
        if email:
            contact.email = email
        if address:
            contact.address = address

    def delete_contact(self, contact):
        self.contacts.remove(contact)


def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            manager.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = manager.search_contact(search_term)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")

        elif choice == '4':
            search_term = input("Enter name or phone number of the contact to update: ")
            results = manager.search_contact(search_term)
            if results:
                contact = results[0]
                print("Current details:")
                print(contact)
                name = input("Enter new name (leave blank to keep current): ")
                phone_number = input("Enter new phone number (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                address = input("Enter new address (leave blank to keep current): ")
                manager.update_contact(contact, name, phone_number, email, address)
                print("Contact updated successfully!")
            else:
                print("No contacts found.")

        elif choice == '5':
            search_term = input("Enter name or phone number of the contact to delete: ")
            results = manager.search_contact(search_term)
            if results:
                contact = results[0]
                manager.delete_contact(contact)
                print("Contact deleted successfully!")
            else:
                print("No contacts found.")

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
