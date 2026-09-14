# 2. Take 10 integers and find sum and average without sum()

numbers = []

# Take 10 integers from the user
for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Find the sum without using sum()
total = 0

for num in numbers:
    total = total + num

# Calculate the average
average = total / 10

# Print the results
print("List:", numbers)
print("Sum:", total)
print("Average:", average)