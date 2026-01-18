#What is meaning of __main__ in Python execution?
# In Python, __main__ is the name of the scope in which top-level code executes.
# When a Python script is run directly, the special variable __name__ is set to "__main__".
# This allows the script to determine if it is being run as the main program or if it
# is being imported as a module in another script. By using the if __name__ == "__main__":
# construct, you can ensure that certain code only runs when the script is executed directly,
# and not when it is imported as a module.
# Example:
def main():
    print("This code runs only when the script is executed directly.")  
if __name__ == "__main__":
    main()