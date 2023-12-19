# Original text with commas

text = "The quick brown fox jumps over then lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)

# Replace word fox with word duck
text = text.replace("fox", "duck")
print(text)

# Remove a word from the sentence, which user decides
user_input = input("Choose a word, which will be removed from the text")
if user_input in text:
    text = text.replace(f'{user_input}',  '')
    print(text)
elif user_input not in text:
    print("Word can not be found in text")


# Count the amount of words in the sentence
def count_words(text):
    words_text = text.split()
    word_count = len(words_text)
    return word_count


# Printout for the word count
print(count_words("The, quick, brown, fox, jumps, over, then, lazy, dog. That \
sentence contains every letter in the English alphabet. Neat!"))

# Remove the commas from the text
text = text.replace(",", "")
print(text)


# Count the amount of characters in sentence, this is without commas
text_length2 = len(text)
print(text_length2)

user_text = input("Give some kind of text here")
if len(user_text) <= 20:
    print(user_text)
else:
    shrt_user_text = user_text[:20] + "..."
    print(shrt_user_text)
