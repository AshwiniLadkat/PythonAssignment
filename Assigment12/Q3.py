#Write a program which accetpt two numbers and prints addition,substraction,multiplication and division of that numbers
def addtion(number1, number2):
    return number1 + number2
def substraction(number1, number2):
    return number1 - number2    
def multiplication(number1, number2):
    return number1 * number2
def division(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Error! Division by zero."
def main():
    print("Enter first number:")
    no1=int(input())
    print("Enter second number:")
    no2=int(input())
    
    sum_result = addtion(no1, no2)
    sub_result = substraction(no1, no2)
    mul_result = multiplication(no1, no2)
    div_result = division(no1, no2)
    
    print(f"Addition of {no1} and {no2} is: {sum_result}")
    print(f"Substraction of {no1} and {no2} is: {sub_result}")
    print(f"Multiplication of {no1} and {no2} is: {mul_result}")
    print(f"Division of {no1} and {no2} is: {div_result}")
if __name__ == "__main__":
    main()