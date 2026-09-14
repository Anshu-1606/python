# 4. Remove Punctuation from String

import string

# Take a string from the user
text = input("Enter a string: ")

# Create an empty string for the result
result = ""

# Check each character
for char in text:
    # Add the character only if it is not punctuation
    if char not in string.punctuation:
        result += char

# Print the string without punctuation
print("String without punctuation:", result)
