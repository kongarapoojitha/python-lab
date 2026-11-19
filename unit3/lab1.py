
# Contact Book Using Lists and Dictionaries

contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {"Name": name, "Phone": phone}
        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for contact in contacts:
                print("Name:", contact["Name"])
                print("Phone:", contact["Phone"])
                print("-------------------")

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["Name"].lower() == search.lower():
                print("Contact Found!")
                print("Name:", contact["Name"])
                print("Phone:", contact["Phone"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Try again.")
