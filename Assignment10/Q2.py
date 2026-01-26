#Write a program which accept number and prints sum of first naturals numbers 
def sumofnaturals(number):
    sum=0
    count=1
    while count <= number:
        sum = sum + count
        count = count + 1
    return sum
def main():
    print("Enter number to print sum of first natural numbers:")
    no=int(input())
    result=sumofnaturals(no)
    print(f"Sum of first {no} natural numbers is: {result}")    
if __name__ == "__main__":
    main()