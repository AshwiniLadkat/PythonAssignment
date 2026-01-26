#write a lamda function using filter() which accepts a list of numbers and returns 
# list of numbers divisible by 3 and 5.

divisibleby3and5  = lambda number :  number if  number % 3 == 0 and number % 5 == 0 else ""
def main(): 
    print("Enter the numbers seperated by , to find number with length equal to 5:")
    listofnumbers = list(map(int, input().split(',')))
    result = list(filter(divisibleby3and5, listofnumbers))
    print("Numbers divisible by 3 and 5 are:")
    print(result)
if __name__ == "__main__":
    main()