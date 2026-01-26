#write a lamda function using filter() which accepts a list of strings and returns list of string 
# having length grater than 5.

stringwithlength5  = lambda inputstr :  inputstr if  len(inputstr ) == 5  else ""
def main():
    print("Enter the strings seperated by , to find string with length equal to 5:")
    inputstrings = list(map(str, input().split(',')))
    result = list(filter(stringwithlength5, inputstrings))
    print("Strings with length equal to 5 from the given list are:")
    print(result)
if __name__ == "__main__":
    main()