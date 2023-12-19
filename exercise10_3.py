import random


# Create a function to open and encode file path to ensure it's correctly interpreted as UTF-8 so there is no errors
# problems with ASCII with help of this function display random verb as Today's Verb to the user
def get_random_proverb(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            verbs_list = [line.strip() for line in file]
        # Create a statement into variable called random_verb = random.choice(verbs_list) to get random verb of the
        # day
        random_verb = random.choice(verbs_list)
        # Create a print to display the random Today's verb to the user
        print(f"Today's verb: {random_verb}.")
    except FileNotFoundError:
        print(f"File not found in: {file_path}")


# Define file path to be used, input your file path for the guestbook, here is mine
file_path = r"C:\Users\Archoste\PycharmProjects\Introduction_Python\School_work\wisewords.txt"

# Call the function to display the random Today's verb from the function
get_random_proverb(file_path)
