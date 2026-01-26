#write a lamda function using filter() which accepts a list of numbers and returns 
# count of even numbers 

from functools import reduce
evennumbers = lambda number : 1 if number % 2 == 0 else 0
def main(): 
    print("Enter the numbers seperated by , to find count of even numbers:")
    listofnumbers = list(map(int, input().split(',')))
    result = list(filter(evennumbers, listofnumbers))
    print("Even numbers of all numbers is:")
    print(result)
    
    print("Count of even numbers is:")
    print(len(result))
if __name__ == "__main__":
    main() 

