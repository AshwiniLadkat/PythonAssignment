#Write number which accpets number and prints cube of that number

def Cube(number):
    return number * number * number 
def main():
    number = int(input("Enter number: "))
    result = Cube(number)
    print("Input is: " + str(number))
    print("Output is: " + str(result))  

if __name__ == "__main__":
    main()
