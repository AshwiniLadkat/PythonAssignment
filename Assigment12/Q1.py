#Write a program which accept character and check whether that character is vowel or not
def checkvowel(character):
    vowels = 'aeiouAEIOU'
    if character in vowels:
        return True
    else:
        return False    
def main():
    print("Enter character to check if it is vowel:")
    char = input().strip()
    if len(char) != 1 or not char.isalpha():
        print("Please enter a single alphabetic character.")
        return
    result = checkvowel(char)
    if result:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")
if __name__ == "__main__":
    main()