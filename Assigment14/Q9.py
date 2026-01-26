#write a lamda fucntion which accept two numbers and returns multiplication
Multiplication  = lambda a,b : a * b
def main():
    print("Enter two numbers to find their multiplication:")
    firstnumber = int(input("Enter first number:"))
    secondnumber = int(input("Enter second number:"))
    result = Multiplication(firstnumber, secondnumber)
    print("Multiplication of the two numbers is :")
    print(result)

if __name__ == "__main__":
    main()