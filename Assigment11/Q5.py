#Write a program which accept one number and check whether it is palindrome or not.
def checkpalindrome(number):
    givenNumber = number
    reversed_num = ""
    while number != 0:
        digit = number % 10
        reversed_num = reversed_num  + str(digit) 
        number = number // 10
    if givenNumber == int(reversed_num):
        return True
    else:
        return False

def main():
    print("Enter number to check if it is palindrome:")
    no = int(input())
    result = checkpalindrome(no)
    if result:
        print(f"{no} is a palindrome.")
    else:
        print(f"{no} is not a palindrome.")

if __name__ == "__main__":
    main()