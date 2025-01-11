# Contact book as a dictionary
contacts = {}

def add_contact():
    """Add a new contact."""
    print("\nAdd New Contact")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if name in contacts:
        print("Contact already exists. Use the update option to modify details.")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    """View all contacts."""
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    print("\nSearch Contact")
    query = input("Enter name or phone number to search: ").strip()

    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["phone"]:
            print(f"\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("No contact found with the given information.")

def update_contact():
    """Update an existing contact."""
    print("\nUpdate Contact")
    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("\nWhat do you want to update?")
    print("1. Phone")
    print("2. Email")
    print("3. Address")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        contacts[name]["phone"] = input("Enter new phone number: ").strip()
    elif choice == "2":
        contacts[name]["email"] = input("Enter new email: ").strip()
    elif choice == "3":
        contacts[name]["address"] = input("Enter new address: ").strip()
    else:
        print("Invalid choice.")
        return

    print(f"Contact '{name}' updated successfully.")

def delete_contact():
    """Delete a contact."""
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

def contact_book():
    """Main menu for the contact book."""
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the contact book
contact_book()
