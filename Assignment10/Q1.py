#Write program which accept number and prints multiplication table of that number.

def multiplicationtable(number):
    count=1
    while count <= 10:
        result=number * count
        print(f"{number} * {count} = {result}")
        count = count + 1
def main():
    print("Enter number to print multiplication table:")
    no=int(input())
    multiplicationtable(no)
if __name__ == "__main__":
    main()  