# Task 7
file = open("marks.txt", "r")
for line in file:
    parts = line.strip().split()
    if len(parts) == 2:
        name, marks = parts
        if int(marks) > 75:
            print(name)
file.close()
