#write a lamda function  which accepts a number and returns Cube of that

Cube = lambda a: a ** a

def main():
    print("Enter a number to calculate cube:")
    number = int(input())          # convert string input to integer
    result = Cube(number)
    print("Cube of the number is:")
    print(result)

if __name__ == "__main__":
    main()
