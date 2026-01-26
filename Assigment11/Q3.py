#write program which accept one number and prints sum of its  digits
def sumofdigits(number):
    sum=0
    while number > 0:
        digit = number % 10        
        sum = sum + digit
        number = number / 10
    return sum
def main():
    print("Enter number to print sum of its digits:")    
    no=int(input())
    result=sumofdigits(no)
    print(f"Sum of digits of {no} is: {result}")    
if __name__ == "__main__":
    main()