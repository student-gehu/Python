file_path = input("Enter the path of the file: ")
# Open the file and read its content
with open(file_path, "r") as file:
    text = file.read()
    text = text.lower()
    words_list = text.split()
    words = []
    for word in words_list:
        if word[0] in 'acdgps':
            words.append(word)
    if words:
        print("Words starting with 'a', 'c', 'd', 'g', 'p', or 's':")
        print(words)
    else:
        print("No words starting with 'a', 'c', 'd', 'g', 'p', or 's' found in the file.")

# output
# Words starting with 'a', 'c', 'd', 'g', 'p', or 's':
# ['crush', 'gunjan', 'during']