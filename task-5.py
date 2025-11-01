
sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("Error: You didn't enter anything!")
else:

    words = sentence.split()

    print("Total number of words:", len(words))