import contacts_file_writer as cfw
class Contacts:
    def __init__(self, contacts=None):
        #Fetches list of contacts from csv file and places it in a list
        contacts = cfw.read_file()
        self.contacts = contacts if contacts else []
         
    #Updates list from csv file
    def reread_files(self):
        self.contacts = cfw.read_file() 
        
    def userid_exists(self, userid):
        for i in self.contacts:
            if i["userid"] == userid:
                return True
        return False
    
    #Adds new contact
    def add_contact(self, userid, name, email, preferred_time):
        #user id must be unique
        if self.userid_exists(userid):
            return ValueError("user id is taken")
        #Sends the new contact to the file writer
        if cfw.append_file(userid, name, email, preferred_time):
            return True
    
    def update_contact(self, userid, name, email, preferred_time):
        #Update the contact in the csv file
        if self.userid_exists(userid):
            if cfw.update_file_entry(userid, name, email, preferred_time):
                return True
        else:
            return f"user does not exists"

    def remove_contact(self, userid):
        #deletes contact from csv file
        if self.userid_exists(userid):
            if cfw.delete_file_entry(userid):
                return True
        else:
            return f"user does not exists"

    #Returns a list of all contacts
    def get_contacts(self):
        if not self.contacts:
            return f"No contacts saved"
        else:
            return self.contacts

    #returns individual contact based on userid   
    def get_contact(self, userid):
        for i in self.contacts:
            if i["userid"] == userid:
                return i
        return f"user does not exists"

    #returns user attribute on request. detail is the name of the attribute        
    def get_contact_detail(self, userid, detail):
        for i in self.contacts:
            if i["userid"] == userid:
                return i[detail]
        return f"user does not exists"