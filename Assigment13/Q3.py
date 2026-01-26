#write a program which accept one number and check whether that number is perfect  or not
def checkperfectnumber(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    else:
        return False
def main():
    print("Enter number to check perfect number or not:")
    no=int(input())
    result=checkperfectnumber(no)
    if result:
        print(f"{no} is a perfect number.")
    else:
        print(f"{no} is not a perfect number.")
if __name__ == "__main__":
    main()