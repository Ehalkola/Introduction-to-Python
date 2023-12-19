import json


# Create a function to print/display of countries and capitals in countries data
def print_countries_and_capitals(data):
    print("All countries and capitals:")
    for entry in data:
        print(f"Country: {entry['country']}, Capital: {entry['capital']}")


# Create a function to filter countries data by starting letter
def filter_by_letter(data, letter):
    filtered_entries = [entry for entry in data if entry['country'].startswith(letter)]
    print(f"Countries and capitals starting with '{letter}':")
    for entry in filtered_entries:
        print(f"Country: {entry['country']}, Capital: {entry['capital']}")


# Define file path to be used, input your file path for the guestbook, here is mine
file_path = r"C:\Users\Archoste\PycharmProjects\Introduction_Python\School_work\countries.json"

# Create while true statement with try/except statements below to open and display/print countries data to the user
while True:
    try:
        with open(file_path, 'r') as file:
            countries_data = json.load(file)
        # Create a display for the user of all the countries and capitals in countries data
        print_countries_and_capitals(countries_data)
        # Create a user input for user to input letter to filter country/capital with starting letter
        user_input = input("Filter a country/capital with a starting letter:\n").upper()
        # Filter and print countries/capitals based on the provided letter
        filter_by_letter(countries_data, user_input)
    # Create except statements if file not found or json.JSONDecodeError, display these if needed
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file '{file_path}'.")
    except ValueError:
        print("Invalid input please try again... Input letters not numbers or special characters...")
