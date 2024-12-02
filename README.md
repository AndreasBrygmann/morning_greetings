# Morning Greetings
Sends out morning greetings to a personalized contact list. The greetings can be automated

## Features
Contact Manager: Read, add, update and delete contacts
Personalized Messages: Creates personalized messages with names and weekdays
Automated sending: Messages are automatically sendt at the contacts preferred time

## Prerequisites
Python 3.x installed on your system.

## Installation
1. Download the package.
2. Unzip
3. Open with IDE or navigate to folder with command line
4. Run command: pip install -e .

## Using the app
1. Run the app with the command: morning_greetings
2. A menu will appear. simply type in the corresponding number for the menu item you want and press enter

### Menu items
1. Send out messages to all users
2. Contacts manager
3. Send a individual message
9. End program

## Project structure
```
morning_greetings/
│
├── morning_greetings/
│   ├── __init__.py
│   ├── main.py                # Entry point for the menu
│   ├── contacts_manager.py
│   ├── contacts_file_writer.py
│   └── contacts.py
│   └── logger.py
│   └── message_generator.py
│   └── message_sender.py
│
├── setup.py                   # Installation script
└── README.md                  # Project documentation (this file)
```

### Files:
#### main.py
Main menu of app

#### message_generator.py
Generates the morning greetings

#### message_sender.py
Sends out the messages

#### contacts.py
Class file for contancts

#### contact_manager.py
Menu for contact manager

#### contacts_file_writer.py
File handler for contacts

#### contacts.csv
File containing your contacts. If the file is missing it will be created when you add your first contact

#### logger.py
Logs stuff




