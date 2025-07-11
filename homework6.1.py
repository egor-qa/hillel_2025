chars = input("Enter some text and I will count the number of unique characters in it:")
unique_chars = set(chars)

print(len(unique_chars))

if len(unique_chars) > 10:
    print(True)
else:
    print(False)