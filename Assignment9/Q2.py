def ChkGreater(number1,number2):
    if number1 > number2:
        return number1  
    else:
        return number2
def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = ChkGreater(number1, number2)
    print("Input is: " + str(number1) + " , " + str(number2))
    print("Output is: " + str(result) + " is greater") 


if __name__ == "__main__":
    main()