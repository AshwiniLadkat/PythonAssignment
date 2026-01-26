#write a lamda function  which accepts a number and returns square of that

Square = lambda a: a * a

def main():
    print("Enter a number to calculate square:")
    number = int(input())          # convert string input to integer
    result = Square(number)
    print("Square of the number is:")
    print(result)

if __name__ == "__main__":
    main()
