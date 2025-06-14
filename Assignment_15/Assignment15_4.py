# Task 4: Compare two files
file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

try:
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    if f1.read() == f2.read():
        print("Success: Files are same.")
    else:
        print("Failure: Files are different.")

    f1.close()
    f2.close()
except FileNotFoundError:
    print("One or both files not found.")
