#write a lamda fucntion which accept two numbers and return maximum number.
maximum  = lambda a,b : a if  a > b else b
def main():
    print("Enter two numbers to find maximum number:")
    firstnumber = int(input("Enter first number:"))
    secondnumber = int(input("Enter second number:"))
    result = maximum(firstnumber, secondnumber)
    print("Maximum number is:")
    print(result)

if __name__ == "__main__":
    main()