# 5. Reverse a list without reverse() or slicing

numbers = []

# Ask how many integers the user wants to enter
n = int(input("How many integers do you want to enter? "))

# Take integers from the user
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Create an empty list for the reversed list
reversed_list = []

# Add elements from the last index to the first
for i in range(n - 1, -1, -1):
    reversed_list.append(numbers[i])

# Print the original and reversed lists
print("Original list:", numbers)
print("Reversed list:", reversed_list)