# Task 1: Check file existence
filename = input("Enter file name: ")

try:
    file = open(filename, "r")
    print(f"{filename} exists.")
    file.close()
except FileNotFoundError:
    print(f"{filename} does not exist.")
