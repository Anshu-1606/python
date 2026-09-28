def even_numbers(limit):
    for num in range(0, limit + 1, 2):
        yield num


for num in even_numbers(10):
    print(num)

# Output
# 0
# 2
# 4
# 6
# 8
# 10