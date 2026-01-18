#Write a program which accepts one number and check whether it is divisible by 3 and 5.

def DivisibleBy3AND5(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return True
    else:
        return False

def main():
    number = int(input("Enter number: "))
    result = DivisibleBy3AND5(number)
    print("Input is: " + str(number))
    print("Output is: " + str(result))

if __name__ == "__main__":
    main()