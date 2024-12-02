import sys
import os

# Ensure the parent directory is in the Python path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))) #Copied from the Games code from

import contact_manager as cm
import message_generator as mg
import message_sender as ms

#Menu works by having the user input a number value for the function they want to run
#Once a number has been inputted the function is called from another module
def main():
    run = True
    while run == True:
        print("_________________________________________________________________")
        print("Welcome to the the morning greeting app. Please select an option:\n")
        print("To send out messages to contactlist enter 1")
        print("For contacts manager enter 2")
        print("To send an indivdual message enter 3\n")
        print("To end program enter 9")
        print("_________________________________________________________________")
        option = input("Enter your number: ")

        if option == "1":
            print(ms.send_messages())
        if option == "2":
            print(cm.menu())
        elif option == "3":
            print(ms.menu())
        elif option == "9":
            run = False
        else:
            print("Please enter a valid option")

if __name__ == "__main__":
    main()