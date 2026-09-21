def remove_last(lst):
    lst.pop()


numbers = [10, 20, 30, 40]

print("Before function:", numbers)

remove_last(numbers)

print("After function:", numbers)

# output
# Before function: [10, 20, 30, 40]
# After function: [10, 20, 30]