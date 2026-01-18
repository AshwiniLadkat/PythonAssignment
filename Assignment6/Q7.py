#What is difference between Parameters and arguments in Python functions?
#ANS-
#Parameters are the variables that are defined in the function definition and act as placeholders for the values that will be passed to the function when it is called. They are specified within the parentheses of the function definition.
#Arguments, on the other hand, are the actual values or data that are passed to the function when it is called. They are provided within the parentheses of the function call and correspond to the parameters defined in the function.
#Here is an example to illustrate the difference:   
def add_numbers(a, b):  # a and b are parameters
    return a + b

result = add_numbers(3, 5)  # 3 and 5 are arguments
print(result)  # Output: 8