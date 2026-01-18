#Can a Python function return multiple values?If yes, how does Python handels it internally?
#ANS- Yes, a Python function can return multiple values. 
# This is handled by returning a tuple containing the values. 
# When a function returns multiple values, Python automatically packs them into a tuple.
def multiple_returns():
    return 1, 2, 3  # Returning multiple values
#When the function is called, the returned tuple can be unpacked into separate variables:
a, b, c = multiple_returns()
print("Returned values are:", a, b, c)  # Output: Returned values are: 1 2 3

