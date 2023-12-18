# Funtion 3
# Create a function _magazine_serial_check(serial), which defines/checks if user input is Valid or Incorrect ISSN
def _magazine_serial_check_(serial):
    valid_serial = "Valid ISSN."
    incorrect_serial = "Incorrect ISSN."
    serial_length = len(serial)
    if serial.isdigit() and serial_length == 8:
        return valid_serial
    else:
        return incorrect_serial


# Create an empty list to add user input into
magazine_list = []
# Create an input to ask user for ISSN-serial, add user input to the list created above
user_input = input("Input an ISSN-serial:\n")
magazine_list.append(user_input)
# Create a for loop to define magazine serials in list with the help of function above, also check if user input
# contains "-" in 4th index +1 , print result to the user
for magazine_serials in magazine_list:
    magazine_serial = magazine_serials.split()
    serial = magazine_serial[0]
    serial_check1 = serial[:5].replace(f"{serial[:4]}", "")
    if serial_check1 == "-":
        serial = magazine_serial[0].replace("-", "")
        result = _magazine_serial_check_(serial)
        print(result)
    else:
        print("Invalid ISSN.")
