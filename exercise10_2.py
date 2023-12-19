import json
from datetime import datetime


# Create a function for the user to read the file,
def read_guestbook(file_path):
    try:
        messages = json.load(open(file_path, "r"))
        [print(f"{message['datetime']} - {message['message']}") for message in messages]
    except FileNotFoundError:
        print("Guestbook is empty.")
    except json.JSONDecodeError:
        print("Guestbook is empty or not in valid JSON format.")


# Create a function for the user to write into the book, add datetime into the beginning of the message and add the
# message into the guestbook
def write_guestbook(file_path, message):
    try:
        messages = json.load(open(file_path, "r"))
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []

    # Import datetime from datetime in format years, months, days and add time in format hours and minutes, add the
    # time in front of the user message and add the new message into the guestbook
    current_datetime = datetime.now().strftime("%Y.%d.%m %H:%M")
    new_message = {"datetime": current_datetime, "message": message}
    messages.append(new_message)
    json.dump(messages, open(file_path, "w"), indent=2)


# Define file path to be used, input your file path for the guestbook, here is mine
file_path = r"C:\Users\Archoste\PycharmProjects\Introduction_Python\School_work\guestbook.txt"

# Create a loop to ask user input, create choice as an input for the user, define if user input is valid (r/w) with,
#  the help of conditional statements, if valid, based on the user input define, which to read or write into the
#  guestbook
while True:
    try:
        choice = input("Do you want to read or write into the guestbook? (r/w):\n")
        if choice == "r":
            read_guestbook(file_path)
        elif choice == "w":
            write_guestbook(file_path, input("Write a new message into the guestbook:\n"))
        else:
            raise ValueError
    except ValueError:
        print("Invalid input, please try again... Input (r to read, w to write).")
