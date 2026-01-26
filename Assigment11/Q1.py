#Write a program which accept number and check wether that number is prime or not 
def checkprimenumber(number):
    isPrime= True
    count=2
    while count < number:
        if number % count == 0:
            isPrime= False
            break
        count = count + 1
    return isPrime
def main():
    print("Enter number to check prime or not:")
    no=int(input())
    result=checkprimenumber(no)
    if result:
        print(f"{no} is a prime number.")
    else:
        print(f"{no} is not a prime number.")
if __name__ == "__main__":
    main()