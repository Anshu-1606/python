def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


c = float(input("Enter temperature in Celsius: "))

print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

#Output
# Enter temperature in Celsius: 38
# Temperature in Fahrenheit: 100.4
