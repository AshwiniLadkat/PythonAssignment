#write a program which accept number and prints all odd numbers till that number
def printoddnumbers(number):
    count=1
    while count <= number:
        if count % 2 != 0:
            print(count)
        count = count + 1
def main():
    print("Enter number to print odd numbers till that number:")    
    no=int(input())
    print("Odd numbers till", no, "are:")
    printoddnumbers (no)
if __name__ == "__main__":
    main()