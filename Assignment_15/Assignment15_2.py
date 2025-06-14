# Task 2: Display file contents
filename = input("Enter file name: ")

try:
    file = open(filename, "r")
    print("File contents:")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")
