# 3. Word Frequency Counter

# Take a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word frequencies
frequency = {}

# Count each word
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print the frequency of each word
for word in frequency:
    print(word + ":", frequency[word])