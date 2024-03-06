contacts = []

def add_contacts():
    contact = {"name": "", "number": 0, "email": "", "favorite": False}
    contact["name"] = str(input("Enter the name: "))
    contact["number"] = int(input("Enter the number: "))
    contact["email"] = str(input("Enter the email: "))

    contacts.append(contact)
    print("\nYour contact has been added successfully!")

def show_contacts():
    print('Added contacts:')
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        print("Name:", contact["name"])
        print("Number:", contact["number"])
        print("Email:", contact["email"])
        print("Favorited?:", "No" if contact["favorite"] == False else "Yes")

def edit_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")    
        print("Name:", contact["name"]) 

    index = int(input("\nEnter the index of the contact you want to edit: ")) - 1
    
    if index >= 0 and index < len(contacts):
        contact = contacts[index]
        # ignore this shit identation, this ''' is a shit bbut i needed
        print('Enter the number of the field you want to edit:')
        print('1. Name | 2. Number | 3. Email')
        choice = int(input('>'))

        if choice == "1":
            contact["name"] = input("Enter the new name: ")
        elif choice == "2":
            contact["number"] = int(input("Enter the new number: "))
        elif choice == "3":
            contact["email"] = input("Enter the new email: ")

def favorite():
   pass

def delete():
   pass
