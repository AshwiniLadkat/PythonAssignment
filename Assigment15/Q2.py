#write lamda function usig filter which accepts a list of numbers and returns a list  of even numbers.
evennumbers = lambda no : no % 2 == 0
def main():
    print("Enter numbers separated by space to find even numbers:")
    numbers = list(map(int, input().split()))
    even_numbers_list = list(filter(evennumbers, numbers))
    print("Even numbers from the given list are:")
    print(even_numbers_list)   
if __name__ == "__main__":
    main() 
