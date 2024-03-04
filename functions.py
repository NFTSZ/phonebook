contacts = []

def add_contacts():
  contact = {"name": "", "number": 0, "email": "", "favorite": False}
  contact["name"] = str(input("Enter the name: "))
  contact["number"] = int(input("Enter the number: "))
  contact["email"] = str(input("Enter the email: "))

  contacts.append(contact)
  print("Your contact has been added successfully!")

def show_contacts():
    pass

def edit():
   pass

def favorite():
   pass

def delete():
   pass
