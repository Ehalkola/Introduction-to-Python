import functions


# Create a function to read and print file from file path
def read_and_print_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read the content of the file into a variable
            content = file.readlines()

            # Print each line with an arrow
            for line in content:
                print(f"-> {line.strip()}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


# Define file path to be used, input your file path for the guestbook, here is mine
file_path = r"C:\Users\Archoste\PycharmProjects\Introduction_Python\School_work\artists.txt"

# Call the function to read and print the file content to the user
functions.read_and_print_file(file_path)
