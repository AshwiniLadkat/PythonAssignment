#what is user defined function ?
#write a function to accept two numbers and return their multiplication
#user defined fucntion  means function defined by user for specific use case
def multiply_numbers(num1, num2):
    """This function takes two numbers as input and returns their multiplication."""
    return num1 * num2  
def main():
    # Accepting two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    # Calling the multiply_numbers function and storing the result
    result = multiply_numbers(number1, number2)
    # Displaying the result
    print("The multiplication of", number1, "and", number2, "is:", result)
if __name__ == "__main__":
    main()