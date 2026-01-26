#Write a lamda function using map() which accepts a list of numbers and returns a list of their squares.

squares= lambda no : no**2
def main():
    print("Enter numbers separated by space to find their squares:")
    numbers = list(map(int, input().split()))
    squares_list = list(map(squares, numbers))
    print("Squares of the given numbers are:")
    print(squares_list)
if __name__ == "__main__":
    main()