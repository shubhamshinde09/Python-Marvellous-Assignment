# print triangle pattern using nested loop
rows = 5  # You can change this value or get input from user
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
