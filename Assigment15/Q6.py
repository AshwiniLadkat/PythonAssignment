#write a lamda function using reduce() which accepts a list of numbers and returns minimun number from that list.

from functools import reduce
maximum  = lambda a,b : b if  a > b else a
def main():
    print("Enter the numbers seperated by , to find maximum number:")
    numbers = list(map(int, input().split(',')))
    result = reduce(maximum, numbers)
    print("Maximum number from the given list is:")
    print(result)
if __name__ == "__main__":
    main()