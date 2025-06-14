# Task 2
filename = "data.txt"
try:
    file = open(filename, "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")
