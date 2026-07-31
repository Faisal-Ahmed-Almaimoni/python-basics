class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.set_phone(phone)
        self.email = email
    
    def set_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            self.__phone = phone
        else:
            raise ValueError("The Phone Number Is Wrong")
    
    def get_phone(self):
        return self.__phone

class AddressBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def show_all_contacts(self):
        for contact in self.contacts:
            print(contact.name, contact.get_phone(), contact.email)

    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if name == contact.name:
                print(contact.name, contact.get_phone(), contact.email)
                found = True
            break

        if not found:
         print("The contact info is not here")


book = AddressBook()
c1 = Contact("Ahmed", "0506731689", "ahmed@gmail.com")
c2= Contact("Mohamed", "0234768539", "mohamed@gmail.com")
book.add_contact(c1)
book.add_contact(c2)

book.show_all_contacts()
book.search_contact("Ahmed")
book.search_contact("Khalid")
