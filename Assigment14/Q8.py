#write a lamda fucntion which accept two numbers and returns addition
Addition  = lambda a,b : a + b
def main():
    print("Enter two numbers to find their addition:")
    firstnumber = int(input("Enter first number:"))
    secondnumber = int(input("Enter second number:"))
    result = Addition(firstnumber, secondnumber)
    print("Addition of the two numbers is :")
    print(result)

if __name__ == "__main__":
    main()