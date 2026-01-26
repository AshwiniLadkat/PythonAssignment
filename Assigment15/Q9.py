#write a lamda function using reduce() which accepts a list of numbers and returns 
# product of all numbers.
from functools import reduce
product = lambda a, b : a * b
def main(): 
    print("Enter the numbers seperated by , to find product of all numbers:")
    listofnumbers = list(map(int, input().split(',')))
    result = reduce(product, listofnumbers)
    print("Product of all numbers is:")
    print(result)
if __name__ == "__main__":
    main()