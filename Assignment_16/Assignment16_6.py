# Task 6
try:
    src = open("source.txt", "r")
    dest = open("destination.txt", "w")
    for line in src:
        dest.write(line)
    print("Copied to destination.txt")
    src.close()
    dest.close()
except FileNotFoundError:
    print("Source file not found.")
