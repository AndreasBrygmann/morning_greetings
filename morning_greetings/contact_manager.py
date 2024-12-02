from contacts import Contacts
import logger
c = Contacts()

#Lets the user input the values of a contacy and makes sure the values are valid
def input_user_values():
    #User is only asked to enter userid if enter_id is True
    run1 = True
    while run1 == True:
        userid = input("Enter user id: ")
        if validate_input(userid): run1 = False 
    run2 = True
    while run2 == True:
        name = input("Enter name: ")
        if validate_input(name): run2 = False
    run3 = True
    while run3 == True:
        email = input("Enter e-mail: ")
        if validate_input(email): run3 = False
    run4 = True
    while run4 == True:
        preferred_time = input("Enter the preferred time: ")
        if validate_input(preferred_time): run4 = False
    
    return userid, name, email, preferred_time

#Checks that a contact value contains no commas
def validate_input(string):
    if "," in string:
        print("contact details cannot contain commas")
        return False
    else:
        return True

def menu():
    print("_________________________________________________________________")
    print("Welcome to the contact manager. Please select an option")
    print("Press 1 to add a new contact")
    print("Press 2 to update a contact")
    print("Press 3 to remove a contact")
    print("Press 4 to find a contact")
    print("Press 5 for a list of all contacts\n")
    print("Press 8 to maually update contacts list from file\n")
    print("Press 9 to return to main menu")
    print("_________________________________________________________________\n")
    option = input("Enter a number... ")

    if option == "1":
        #Sends user to function that enters and checks user info
        userid,name,email,preferred_time = input_user_values()
        if c.add_contact(userid,name,email,preferred_time):
            logger.log_new_user(userid)
            print("Contact added")
            c.reread_files()

    elif option == "2":
        userid,name,email,preferred_time = input_user_values()
        if c.update_contact(userid,name,email,preferred_time):
            logger.log_update_user(userid)
            print("Contact updated")
            c.reread_files()

    elif option == "3":
        userid = input("Enter the user id of the contact you want to delete: ")
        if c.remove_contact(userid):
            logger.log_delete_user(userid)
            print("Contact deleted")
            c.reread_files()

    elif option == "4":
        userid = input("Enter the user id of the contact you want to find: ")
        print(c.get_contact(userid))

    elif option == "5":
        for row in c.get_contacts():
            print(row)

    elif option == "8":
        c.reread_files()
        print("Updated contact list")

    elif option == "9":
        return
    
    else:
        print("Please select a valid option\n")
        menu()