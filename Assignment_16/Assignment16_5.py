# Task 5
filename = input("Enter file name: ")
try:
    file = open(filename, "r")
    for line in file:
        if len(line.split()) > 5:
            print(line.strip())
    file.close()
except FileNotFoundError:
    print("File not found.")
