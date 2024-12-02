import datetime

#Generates a message with the name of the user and the current weekday
def generate_message(name):
    if not name:
        raise ValueError("Name address is missing")
    weekday = datetime.datetime.now().strftime("%A")
    return f"Good morning {name}, today is {weekday}. Have an excellent day!"