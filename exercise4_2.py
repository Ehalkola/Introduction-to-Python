# Input
# Ask input from the user
user_input = input("Give some text")
reversed_input = user_input[::-1]
print(reversed_input)


#  Create a function called is palindrome to determine if user input is palindrome
def is_palindrome(user_input):
    text = user_input.replace(" ", "")

    # Return the text
    return text == text[::-1]


# How to check if palindrome == text
if not user_input:
    print("Your text is empty")
elif is_palindrome(user_input):
    print("PALINDROME: YES")
else:
    print("PALINDROME: NO")
