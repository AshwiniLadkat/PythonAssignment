#Write a program which accept one number and prints that many numbers start from 1
def printnumbersfrom1(number):
    count = 1
    print("First {number} numbers are:")
    while count <= number:
        print(count)
        count += 1
def main():
    print("Enter number to print numbers from 1:")
    no=int(input())
    printnumbersfrom1(no)
if __name__ == "__main__":
    main()