import message_generator as mg
import logger
from contacts import Contacts
c = Contacts()

#sends a single message to one contact
def send_message(email, message):
    if not email:
        raise ValueError("Email address is missing")
    # Simulate sending a message (replace this with actual email sending logic if needed)
    print(f"Sending message to {email}: {message}")
    return True

#sends messages to all contacts at once
def send_messages():
    if not c.contacts:
        raise IndexError("No Contacts")
    for row in c.contacts:
        send_message(row["email"], mg.generate_message(row["name"]))
        logger.log_message(row["userid"], mg.generate_message(row["name"]))
    print(f"Messages sent out to {len(c.contacts)} contacts")
    
#user input for sending single message
def menu():
    print("Welcome to the message sender")
    userid = input("Please enter the userid of the user you want to send the message to: ")
    if c.userid_exists(userid):
        name = c.get_contact_detail(userid, "name")
        email = c.get_contact_detail(userid, "email")
        messg = mg.generate_message(name)
        if send_message(email, messg):
            logger.log_message(userid, messg)
        else:
            return f"Could not send message"
    else:
        return ValueError("No contact with this userid")