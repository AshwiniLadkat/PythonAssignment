#Write a program which accept number and  prints factorial of that number
def calculatefactorial(number):
    fact = 1
    count = 1
    while count <= number:
        fact = fact * count
        count = count + 1
    return fact

def main():
    print("Enter number to print factorial:")
    no=int(input())
    result=calculatefactorial(no)
    print(f"Factorial of {no} is: {result}")

if __name__ == "__main__":
    main()  