# Task 3
filename = input("Enter file name: ")
try:
    file = open(filename, "r")
    content = file.read()
    lines = content.splitlines()
    words = content.split()
    chars = len(content)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", chars)
    file.close()
except FileNotFoundError:
    print("File not found.")
