from contact import Contact
from contact_book import ContactBook

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            print("\nAll Contacts:")
            contact_book.display_all_contacts()

        elif choice == '3':
            name_to_search = input("Enter name to search: ")
            found_contact = contact_book.search_contact(name_to_search)
            if found_contact:
                print("\nContact found:")
                found_contact.display_contact()
            else:
                print("Contact not found.")

        elif choice == '4':
            name_to_update = input("Enter name of contact to update: ")
            new_name = input("Enter new name (or press Enter to keep current): ")
            new_phone = input("Enter new phone number (or press Enter to keep current): ")
            new_email = input("Enter new email (or press Enter to keep current): ")
            contact_book.update_contact(name_to_update, 
                                        new_name if new_name else None,
                                        new_phone if new_phone else None,
                                        new_email if new_email else None)
        
        elif choice == '5':
            name_to_delete = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name_to_delete)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            contact_book.close_connection()
            break

        else:
            print("Invalid choice. Please enter a valid option.")

main()
