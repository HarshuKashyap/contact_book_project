import json
import os

CONTACT_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, 'r') as file:
        return json.load(file)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    contacts = load_contacts()
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n📇 Contact List:")
        for idx, c in enumerate(contacts, start=1):
            print(f"{idx}. {c['name']} - {c['phone']} - {c['email']}")
    print()

# Search contact by name
def search_contact():
    search = input("🔍 Enter name to search: ").lower()
    contacts = load_contacts()
    found = [c for c in contacts if search in c['name'].lower()]
    
    if found:
        print("🔎 Results:")
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
    else:
        print("❌ No contact found with that name.")
    print()

# Update contact
def update_contact():
    name = input("✏️ Enter name to update: ")
    contacts = load_contacts()
    
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("Enter new phone: ")
            c['email'] = input("Enter new email: ")
            save_contacts(contacts)
            print("✅ Contact updated!\n")
            return
    print("❌ Contact not found.\n")

# Delete contact
def delete_contact():
    name = input("🗑️ Enter name to delete: ")
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    
    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print("✅ Contact deleted!\n")
    else:
        print("❌ Contact not found.\n")

# Menu
def menu():
    while True:
        print("\n======= 📒 Contact Book Menu =======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Exiting... Bye!")
            break
        else:
            print("⚠️ Invalid choice. Try again!\n")

# Run the app
if __name__ == "__main__":
    menu()
