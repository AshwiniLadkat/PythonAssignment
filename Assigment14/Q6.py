#write a lamda fucntion which accept one number and returns True if number is Odd otherwise False 
oddnumber  = lambda a : True if a % 2 != 0 else False
def main():
    print("Enter a number to check if it is odd:")
    number = int(input("Enter number:"))
    result = oddnumber(number)
    print("Is the number odd?:")
    print(result)

if __name__ == "__main__":
    main()