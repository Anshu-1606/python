def change_string(s):
    s = "X" + s[1:]
    print("Inside function:", s)


text = "Hello"

print("Before function:", text)

change_string(text)

print("After function:", text)