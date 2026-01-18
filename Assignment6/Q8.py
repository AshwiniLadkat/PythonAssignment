#what happens if the number of arguments  does not match the number of parameters in a function call?
#If the number of arguments does not match the number of parameters in a function call, 
# Python will raise a TypeError.
#This error indicates that the function was called with an incorrect number of arguments.
#For example, if a function is defined to take two parameters but is called with only one argument, Python will raise an error like this:
def example_function(a, b):
    return a + b
#example_function(5)  # This will raise a TypeError
#Similarly, if a function is defined to take two parameters but is called with three arguments,
# Python will also raise a TypeError:
#example_function(5, 10, 15)  # This will also raise a TypeError.