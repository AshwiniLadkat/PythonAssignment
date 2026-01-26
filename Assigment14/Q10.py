#write a lamda fucntion which accept three numbers and returns largest number

largestnumber  = lambda a,b,c : a if (a > b and a > c) else (b if b > c else c)
def main():
    print("Enter two numbers to find their addition:")
    firstnumber = int(input("Enter first number:"))
    secondnumber = int(input("Enter second number:"))
    thirdnumber = int(input("Enter third number:"))
    result = largestnumber(firstnumber, secondnumber, thirdnumber)
    print("Largest of the three numbers is :")
    print(result)

if __name__ == "__main__":
    main()