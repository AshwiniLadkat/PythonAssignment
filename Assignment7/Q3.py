#Explain the use of Global keyword.When should it be used ?
#The `global` keyword in Python is used to declare that a variable inside a function
# is referring to a global variable (a variable defined outside of the function)
# rather than creating a new local variable with the same name.
#When to use the `global` keyword:
#1. Modifying Global Variables: If you need to modify the value of a global variable
# from within a function, you must use the `global` keyword to indicate that you are
# referring to the global variable and not creating a new local variable.
#Example:
counter = 0  # Global variable
def increment_counter():
    global counter  # Declare that we are using the global variable 'counter'
    counter += 1    # Modify the global variable
increment_counter()
print(counter)  # Output: 1


 