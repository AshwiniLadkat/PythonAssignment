#Write a lamda fucntiond usig filter which accepts a list of numbers and returns a list  of odd numbers.
oddnumbers = lambda no : no % 2 != 0
def main():
    print("Enter numbers separated by space to find odd numbers:")
    numbers = list(map(int, input().split()))
    odd_numbers_list = list(filter(oddnumbers, numbers))
    print("Odd numbers from the given list are:")
    print(odd_numbers_list)
if __name__ == "__main__":
    main()