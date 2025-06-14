# Task 4
file = open("numbers.txt", "w")
for i in range(10):
    num = input(f"Enter number {i+1}: ")
    file.write(num + "\n")
file.close()
print("Numbers written to numbers.txt")
