# Task 3: Copy contents from one file to Demo.txt
source_file = input("Enter source file name: ")

try:
    src = open(source_file, "r")
    dest = open("Demo.txt", "w")
    
    for line in src:
        dest.write(line)

    print(f"Contents copied from {source_file} to Demo.txt")
    src.close()
    dest.close()
except FileNotFoundError:
    print("Source file not found.")
