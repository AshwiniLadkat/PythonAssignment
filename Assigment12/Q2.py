#Write a program which accept number and prints its factors
def printfactors(number):
    count = 1
    print("Factors of {number} are:")
    while count <= number:
        if number % count == 0:
            print(count)
        count += 1  
def main():
    print("Enter number to print its factors:")
    no=int(input())
    printfactors(no)
if __name__ == "__main__":
    main()