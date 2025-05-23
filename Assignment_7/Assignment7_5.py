ChkPalindrome = lambda C : C == C[::-1]

def main():
    print("Enter a string : ")
    ch = input()

    s = ChkPalindrome(ch)
    if s:
        print(ch + " is a palindrome")
    else:
        print(ch + " is not a palindrome")

if __name__ == "__main__":
    main()