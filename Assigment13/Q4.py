#Write a program which accept one number and prints binary equivalent of that number
def printbinaryequivalent(number):
    if number == 0:
        print("Binary equivalent of 0 is: 0")
        return
    binary = ""
    n = number
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    print(f"Binary equivalent of {number} is: {binary}")
def main():
    print("Enter number to print binary equivalent:")
    no=int(input())
    printbinaryequivalent(no)
if __name__ == "__main__":
    main()