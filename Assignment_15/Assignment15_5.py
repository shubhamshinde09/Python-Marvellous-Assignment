# Task 5: Count frequency of a word/string in file
filename = input("Enter file name: ")
search_word = input("Enter string to search: ")

try:
    file = open(filename, "r")
    content = file.read()
    count = content.count(search_word)
    print(f"The string '{search_word}' appears {count} times.")
    file.close()
except FileNotFoundError:
    print("File not found.")
