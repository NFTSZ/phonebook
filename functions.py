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

def edit():
   pass

def favorite():
   pass

def delete():
   pass
