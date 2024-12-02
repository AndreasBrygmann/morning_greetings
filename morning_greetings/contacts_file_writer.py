import os

#Reads csv file and puts the contacts into a dictionary
def read_file():
    contacts = []
    if os.path.isfile("contacts.csv"): #Checks that file exists. If no file has been created yet, an empty list is returned
        with open("contacts.csv", "r") as contacts_file:
            contactline = contacts_file.readline().rstrip("'").rstrip("\n")
            while contactline !="":
                contactsplit = contactline.split(",") #splits lines by commas to isolate values
                #assigns the values to dictionary
                contact = {
                    "userid": contactsplit[0],
                    "name": contactsplit[1],
                    "email": contactsplit[2],
                    "preferred_time" : contactsplit[3]
                }
                contacts.append(contact)

                contactline = contacts_file.readline().rstrip("'").rstrip('\n')
    return contacts

#Adds contact to the csv file
def append_file(userid, name, email, preferred_time):
    with open("contacts.csv", "a") as contacts_file:
        contact = f'{userid},{name},{email},{preferred_time}'
        contacts_file.write(contact)
        contacts_file.write("\n")
        return True

 #Deletes a contact by overwriting the contacts file with all contacts exept the one to be deleted
def delete_file_entry(userid):
    with open("contacts.csv", "r") as contacts_file:
        contacts = contacts_file.readlines()
    with open("contacts.csv", "w") as contacts_file:
        for c in contacts:
            if c.strip("\n").partition(",")[0] != userid: #Isolates the userid to find the contact to be exluded from the new file
                contacts_file.write(c)
    return True

#Deletes old contact and appends updated contact
def update_file_entry(userid, name, email, preferred_time):
    delete_file_entry(userid)
    append_file(userid, name, email, preferred_time)
    return True