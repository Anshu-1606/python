def maximum(a, b):
    if a > b:
        return a
    else:
        return b


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Maximum:", maximum(x, y))

# Output
# Enter first number: 25
# Enter second number: 35
# Maximum: 35