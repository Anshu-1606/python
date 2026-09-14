# 3. Remove duplicates while preserving order

numbers = []

# Ask how many integers the user wants to enter
n = int(input("How many integers do you want to enter? "))

# Take integers from the user
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Create a new list for unique numbers
unique_numbers = []

# Add only numbers that are not already in the list
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Print the original and updated lists
print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)