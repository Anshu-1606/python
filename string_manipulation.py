# 1. String Manipulation

# Take a string from the user
text = input("Enter a string: ")

# Convert the string to uppercase
print("Uppercase:", text.upper())

# Convert the string to lowercase
print("Lowercase:", text.lower())

# Reverse the string
print("Reverse:", text[::-1])

# Count the number of vowels
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


