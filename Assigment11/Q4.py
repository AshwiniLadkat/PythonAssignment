#write program which accept one number and prints reverse of that number
def reverse_number(number):
    reversed_num = ""
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num  + str(digit) 
        number = number // 10
    return reversed_num    
def main():
    print("Enter number to print its reverse:")
    no = int(input())
    result = reverse_number(no) 
    print(f"Reverse of {no} is: {result}")

if __name__ == "__main__":
    main()