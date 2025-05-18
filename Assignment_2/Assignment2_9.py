def NoOfDigit(no):
                    count = 0
                    if no == 0:
                            return 1
                    while no != 0:
                            count = count + 1
                            no = no // 10
                    return count
                                           

num = int(input("Enter a number you want : "))

a = NoOfDigit(num)
print("The total digits in the given number is : ",a)