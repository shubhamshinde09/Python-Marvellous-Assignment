# Vowel or Consonant Check
char = input("Enter a character: ").lower()

if char in 'aeiou' and len(char) == 1 and char.isalpha():
    print(f"'{char}' is a vowel.")
else:
    print(f"'{char}' is a consonant.")
