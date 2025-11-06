
words = input("Enter a sentence: ")

if words.strip() == "":
    print("Error: You didn't enter anything!")
else:

    words = words.split()

    print("Total number of words:", len(words))