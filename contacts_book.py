contacts = []
for i in range(2):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
for contact in contacts:
    print(contact["name"] , " - " , contact["phone"])
    
