# Task 1
file = open("student.txt", "w")
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    file.write(name + "\n")
file.close()
print("Names written to student.txt")
