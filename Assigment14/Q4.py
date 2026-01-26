#write a lamda fucntion which accept two numbers and return minimum number.
minimum  = lambda a,b : a if  a < b else b
def main():
    print("Enter two numbers to find minimum number:")
    firstnumber = int(input("Enter first number:"))
    secondnumber = int(input("Enter second number:"))
    result = minimum(firstnumber, secondnumber)
    print("Minimum number is:")
    print(result)

if __name__ == "__main__":
    main()