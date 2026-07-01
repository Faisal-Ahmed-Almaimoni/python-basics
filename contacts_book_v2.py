name = input("ENter name: ")
phone = input("Enter phone number: ")

file = open("contacts.txt", "a")
file.write(name +" - " +phone +"\n")
file.close()


file = open("contacts.txt", "r")
print(file.read())
file.close()
