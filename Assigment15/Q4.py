#Write lamda function using reduce() which accepts a list of numbers and returns teh addition of all elements.

from functools import reduce    
addition = lambda a, b : a + b
def main():
    print("Enter the numbers seperated by , to find their addition:")
    numbers = list(map(int, input().split(',')))
    result = reduce(addition, numbers)
    print("Addition of the given numbers is:")
    print(result)
if __name__ == "__main__":
    main()