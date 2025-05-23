# Accept input from the user Print factorial of a number using a for loop

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is: {factorial}")
