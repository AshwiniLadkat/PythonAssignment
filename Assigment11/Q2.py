#Write a program which accept number and prints the count of digits in that number
def countofdigits(number):
    count = 0
    if number == 0:
        return 1
    while number != 0:
        number = number // 10
        count = count + 1
    return count
def main():
    print("Enter number to print count of digits:")
    no=int(input())
    result=countofdigits(no)
    print(f"Count of digits in {no} is: {result}")

if __name__ == "__main__":
    main()