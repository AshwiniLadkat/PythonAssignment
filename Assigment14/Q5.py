#write a lamda fucntion which accept one number and returns True if number is even otherwise False 
evennumber  = lambda a : True if a % 2 == 0 else False
def main():
    print("Enter a number to check if it is even:")
    number = int(input("Enter number:"))
    result = evennumber(number)
    print("Is the number even?:")
    print(result)

if __name__ == "__main__":
    main()