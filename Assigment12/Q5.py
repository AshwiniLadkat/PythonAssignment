#Write a program which accept one number and prints that many numbers in reverse order
def printnumbersinreverse(number):
    count = number
    print(f"First {number} numbers in reverse order are:")
    while count >= 1:
        print(count)
        count -= 1
def main():
    print("Enter number to print numbers in reverse order:")
    no=int(input())
    printnumbersinreverse(no)
if __name__ == "__main__":
    main()  