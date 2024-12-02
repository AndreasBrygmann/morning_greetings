import datetime

#This module logs events to two different log files: message_log.txt and user_log.txt

def log_message(userid, message):
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"Timestamp: {datetime.datetime.now()} | User ID: {userid} | Message: {message}\n")

def log_new_user(userid):
    with open("user_log.txt", "a") as log_file:
        log_file.write(f"new user added on: {datetime.datetime.now()} | User ID: {userid}\n")

def log_delete_user(userid):
    with open("user_log.txt", "a") as log_file:
        log_file.write(f"user deleted on: {datetime.datetime.now()} | User ID: {userid}\n")

def log_update_user(userid):
    with open("user_log.txt", "a") as log_file:
        log_file.write(f"user updated on: {datetime.datetime.now()} | User ID: {userid}\n")