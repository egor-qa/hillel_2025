while "True":
    text = input("Enter text that contains words with 'h' or 'H' letters:")
    for char in text:
        if char == 'h' or char == 'H':
            print("Successfully!")
            exit()