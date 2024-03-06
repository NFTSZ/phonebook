contacts = []

def add_contacts():
    contact = {"name": "", "number": 0, "email": "", "favorite": False}
    contact["name"] = input("Enter the name: ")
    contact["number"] = input("Enter the number: ")
    contact["email"] = input("Enter the email: ")

    contacts.append(contact)
    print("\nYour contact has been added successfully!")

def show_all_contacts():
    if len(contacts) > 0:
        print('Added contacts:')
        for i, contact in enumerate(contacts, start=1):
            print(f"\nContact {i}:")
            print("Name:", contact["name"])
            print("Number:", contact["number"])
            print("Email:", contact["email"])
            print("Favorited?:", "No" if contact["favorite"] == False else "Yes")
    else:
        print("You have no contacts yet")

def edit_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")    
        print("Name:", contact["name"]) 

    index = int(input("\nEnter the index of the contact you want to edit: ")) - 1
    
    if index >= 0 and index < len(contacts):
        contact = contacts[index]
        print('Enter the number of the field you want to edit:')
        print('1. Name | 2. Number | 3. Email')
        choice = int(input('> '))

        if choice == 1:
            contact["name"] = input("Enter the new name: ")
        elif choice == 2:
            contact["number"] = int(input("Enter the new number: "))
        elif choice == 3:
            contact["email"] = input("Enter the new email: ")
    print("Contact edited successfully")

def favorite_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")    
        print("Name:", contact["name"]) 

    index = int(input("\nEnter the index of the contact you want to favorite: ")) - 1
   
    if index >= 0 and index < len(contacts):
        contact = contacts[index]

        if contact["favorite"] == False:
            choice = input("Mark this contact as favorite? yes/no > ").lower()
            if choice == "yes":
                contact["favorite"] = True
                print("Added this contact to favorites")
            else:
                print("This contact is not favorited.")
        else:
            choice = input("This contact is favorited, do you want to unmark it? yes/no > ").lower()
            if choice == "yes":
                contact["favorite"] = False
                print("This contact is not favorited.")
            else:
                print("the contact remains in the favorites list")

def view_favorite_list():
    favorite_contacts = [contact for contact in contacts if contact["favorite"]] # list comprehension
    
    if favorite_contacts:
        print('Favorite contacts:')
        for i, contact in enumerate(favorite_contacts, start=1):
            print(f"\nContact {i}:")
            print("Name:", contact["name"])
            print("Number:", contact["number"])
            print("Email:", contact["email"])
            print("Favorited?:", "Yes")
    else:
        print("You have no favorite contacts yet")


def delete_contacts():
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")    
        print("Name:", contact["name"]) 

    index = int(input("\nEnter the index of the contact you want to delete: ")) - 1
    
    if index >= 0 and index < len(contacts):
        choice = input("Are you sure? yes/no > ").lower()
        if choice == "yes":
            del contacts[index]
            print("The contact has been removed from the list")
        else:
            print("Your contact remains saved")