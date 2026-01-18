#Write a program which accepts one number and prints square of that number
def Square(number):
    return number * number  
def main():
    number = int(input("Enter number: "))
    result = Square(number)
    print("Input is: " + str(number))
    print("Output is: " + str(result))      
    
if __name__ == "__main__":
    main()