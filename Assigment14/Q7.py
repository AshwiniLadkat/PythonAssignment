#write a lamda fucntion which accept one number and returns True if divisible by 5 otherwise False
divisible_by_5  = lambda a : True if a % 5 == 0 else False
def main():
    print("Enter a number to check if it is divisible by 5:")
    number = int(input("Enter number:"))
    result = divisible_by_5(number)
    print("Is the number divisible by 5?:")
    print(result)

if __name__ == "__main__":
    main()