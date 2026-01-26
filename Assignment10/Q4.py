#write a program which accept number and prints all even numbers till that number
def printevennumbers(number):
    count=1
    while count <= number:
        if count % 2 == 0:
            print(count)
        count = count + 1
def main():
    print("Enter number to print even numbers till that number:")    
    no=int(input())
    print("Even numbers till", no, "are:")
    printevennumbers(no)
if __name__ == "__main__":
    main()